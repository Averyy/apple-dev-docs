"""Apple JSON -> markdown: the converter's rendering of DocC's JSON.

Each test renders a small page (the shapes Apple's live JSON has) through the
scraper's own _extract_from_json and AppleDocMarkdownConverter.convert_page.
"""

import inspect
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

import pytest

from scraper.config import Config
from scraper.json_scraper import (
    KNOWN_BLOCK_TYPES, KNOWN_INLINE_TYPES, AppleJSONDocumentationScraper, apply_json_patch)
from scraper.utils import assets
from scraper.utils.markdown_converter import join_blocks, labeled, quote_blocks

URL = "https://developer.apple.com/documentation/testkit/widget"
SWIFT_PLATFORMS = ["iOS", "macOS"]


@pytest.fixture
def scraper(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> AppleJSONDocumentationScraper:
    monkeypatch.setattr(Config, "OUTPUT_DIR", tmp_path / "documentation")
    monkeypatch.setattr(Config, "CACHE_DIR", tmp_path / ".hashes")
    return AppleJSONDocumentationScraper("TestKit", "Test Kit")


def text(value: str) -> Dict[str, Any]:
    return {"type": "text", "text": value}


def para(*inline: Any) -> Dict[str, Any]:
    return {"type": "paragraph", "inlineContent": [text(i) if isinstance(i, str) else i for i in inline]}


def tokens(code: str) -> List[Dict[str, str]]:
    return [{"kind": "text", "text": code}]


def declaration(code: str, languages: Optional[List[str]] = None, platforms: Optional[List[str]] = None,
                **extra: Any) -> Dict[str, Any]:
    return {"languages": languages or ["swift"], "platforms": platforms or SWIFT_PLATFORMS,
            "tokens": tokens(code), **extra}


def page(sections: Optional[List[Dict[str, Any]]] = None, **top: Any) -> Dict[str, Any]:
    metadata = {"title": "Widget", "symbolKind": "struct", "roleHeading": "Structure",
                "platforms": [{"name": "iOS", "introducedAt": "17.0"}]}
    metadata.update(top.pop("metadata", {}))
    return {"identifier": {"url": "doc://com.apple.testkit/documentation/TestKit/Widget", "interfaceLanguage": "swift"},
            "kind": "symbol", "schemaVersion": {"major": 0}, "sections": [], "metadata": metadata,
            "primaryContentSections": sections or [], "references": top.pop("references", {}), **top}


def render(scraper: AppleJSONDocumentationScraper, json_page: Dict[str, Any], url: str = URL) -> str:
    return scraper.markdown_converter.convert_page(scraper._extract_from_json(scraper.sink, json_page, url))


def content(*blocks: Dict[str, Any]) -> Dict[str, Any]:
    return {"kind": "content", "content": list(blocks)}


def topic(title: str, url: str, **extra: Any) -> Dict[str, Any]:
    return {"type": "topic", "kind": "symbol", "role": "symbol", "title": title, "url": url, **extra}


def warnings_of(monkeypatch: pytest.MonkeyPatch) -> List[Dict[str, Any]]:
    """The WARNs json_scraper logs from now on, each {event, **fields}."""
    warnings: List[Dict[str, Any]] = []

    class Logger:
        def warning(self, event: str, **kw: Any) -> None:
            warnings.append(dict(kw, event=event))

    monkeypatch.setattr("scraper.json_scraper.logger", Logger())
    return warnings


# A list and a code listing, the blocks that can't share a line with a label
LIST = {"type": "unorderedList", "items": [{"content": [para("a")]}, {"content": [para("b")]}]}
CODE = {"type": "codeListing", "syntax": "swift", "code": ["let x = 1", "", "let y = 2"]}


class TestAssets:
    def test_hosting_root_is_the_prefix_before_data(self) -> None:
        assert assets.hosting_root("https://developer.apple.com/tutorials/data/documentation") == \
            "https://developer.apple.com/tutorials"
        assert assets.hosting_root("https://developer.apple.com/tutorials/data/design") == \
            "https://developer.apple.com/tutorials"

    def test_root_relative_urls_go_under_the_hosting_root(self) -> None:
        root = "https://developer.apple.com/tutorials"
        assert assets.asset_url("/images/com.apple.Swift/a@2x.png", root) == \
            "https://developer.apple.com/tutorials/images/com.apple.Swift/a@2x.png"
        assert assets.asset_url("https://docs-assets.developer.apple.com/x.png", root) == \
            "https://docs-assets.developer.apple.com/x.png"

    def test_variant_preference(self) -> None:
        dark2x = {"traits": ["2x", "dark"], "url": "/d2"}
        light1x = {"traits": ["1x", "light"], "url": "/l1"}
        light2x = {"traits": ["2x", "light"], "url": "/l2"}
        plain = {"traits": ["1x"], "url": "/p1"}
        assert assets.pick_variant([dark2x, light1x, light2x]) is light2x
        assert assets.pick_variant([dark2x, light1x]) is light1x
        assert assets.pick_variant([plain, {"traits": ["3x"], "url": "/p3"}]) is plain
        assert assets.pick_variant([]) is None
        assert assets.variant_url({"variants": [dark2x, light1x]}, "https://h/t") == "https://h/t/l1"
        assert assets.variant_url({}, "https://h/t") == ""


class TestJsonPatch:
    def test_operations_on_a_copy(self) -> None:
        doc = {"a": {"b": [1, 2]}, "c~/d": 1}
        patched = apply_json_patch(doc, [
            {"op": "replace", "path": "/a/b/0", "value": 9},
            {"op": "add", "path": "/a/b/-", "value": 3},
            {"op": "add", "path": "/a/b/1", "value": 5},
            {"op": "remove", "path": "/c~0~1d"},
            {"op": "add", "path": "/e", "value": {"f": 1}},
        ])
        assert patched == {"a": {"b": [9, 5, 2, 3]}, "e": {"f": 1}}
        assert doc == {"a": {"b": [1, 2]}, "c~/d": 1}

    def test_whole_document_and_errors(self) -> None:
        assert apply_json_patch({"a": 1}, [{"op": "replace", "path": "", "value": {"b": 2}}]) == {"b": 2}
        with pytest.raises(KeyError):
            apply_json_patch({"a": 1}, [{"op": "replace", "path": "/x/y", "value": 1}])
        with pytest.raises(ValueError):
            apply_json_patch({"a": 1}, [{"op": "move", "path": "/a", "from": "/b"}])


class TestLayoutHelpers:
    def test_join_blocks(self) -> None:
        assert join_blocks([], 2) == ""
        # Every line after the first is indented, a single block's too
        assert join_blocks(["one\ntwo"], 2) == "one\n  two"
        assert join_blocks(["- a\n- b"], 2) == "- a\n  - b"
        assert join_blocks(["a", "```swift\nx\n\ny\n```"], 3) == "a\n\n   ```swift\n   x\n\n   y\n   ```"

    def test_labeled(self) -> None:
        assert labeled("- `x`:", "Text.\n\n  More.", 2) == "- `x`: Text.\n\n  More."
        assert labeled("- `x`:", "", 2) == "- `x`: "
        # A list, code listing, table, quote or heading first goes after a blank line
        assert labeled("- `x`:", "- a\n  - b", 2) == "- `x`:\n\n  - a\n  - b"
        assert labeled("- `x`:", "1. a", 2) == "- `x`:\n\n  1. a"
        assert labeled("- `x`:", "```swift\n  x\n  ```", 2) == "- `x`:\n\n  ```swift\n  x\n  ```"
        for block in ("| a |", "> a", "#### A"):
            assert labeled("- `x`:", block, 2) == f"- `x`:\n\n  {block}"
        for text in ("-1 is none.", "**Bold**", "`code`", "```Task/isCancelled``", "![](a.png)", "#selector"):
            assert labeled("- `x`:", text, 2) == f"- `x`: {text}"

    def test_quote_blocks(self) -> None:
        assert quote_blocks("**Note**:", ["a"]) == "> **Note**: a"
        assert quote_blocks("**Note**:", ["a\nb"]) == "> **Note**: a\n> b"
        assert quote_blocks("**Note**:", ["a", "- b\n- c"]) == "> **Note**: a\n>\n> - b\n> - c"
        assert quote_blocks("**Note**:", ["- b\n- c"]) == "> **Note**:\n>\n> - b\n> - c"
        assert quote_blocks("**Note**:", ["```\nx\n\ny\n```"]) == "> **Note**:\n>\n> ```\n> x\n>\n> y\n> ```"


class TestDeclarations:
    def test_one_swift_declaration(self, scraper: AppleJSONDocumentationScraper) -> None:
        md = render(scraper, page([{"kind": "declarations", "declarations": [declaration("struct Widget")]}]))
        assert "## Declaration\n\n```swift\nstruct Widget\n```\n\n" in md

    def test_every_declaration_gets_its_fence(self, scraper: AppleJSONDocumentationScraper) -> None:
        md = render(scraper, page([{"kind": "declarations", "declarations": [
            declaration("func read(completion: @escaping () -> Void)"),
            declaration("func read() async throws"),
        ]}]))
        assert "```swift\nfunc read(completion: @escaping () -> Void)\n```\n\n```swift\nfunc read() async throws\n```" in md
        assert "*iOS, macOS*" not in md

    def test_data_declaration_has_no_language_tag(self, scraper: AppleJSONDocumentationScraper) -> None:
        md = render(scraper, page([{"kind": "declarations", "declarations": [
            declaration("string status", languages=["data"], platforms=["Unsupported OS: App Store Server API"])]}]))
        assert "## Declaration\n\n```\nstring status\n```" in md

    def test_occ_declarations_on_different_platforms_are_labeled(self, scraper: AppleJSONDocumentationScraper) -> None:
        md = render(scraper, page([{"kind": "declarations", "declarations": [
            declaration("bool merge(const OSDictionary *otherDictionary);", ["occ"], ["DriverKit"]),
            declaration("virtual bool merge(const OSDictionary *aDictionary);", ["occ"], ["macOS"]),
        ]}]))
        assert ("## Declaration\n\n*DriverKit*\n\n```cpp\nbool merge(const OSDictionary *otherDictionary);\n```\n\n"
                "*macOS*\n\n```cpp\nvirtual bool merge(const OSDictionary *aDictionary);\n```") in md

    def test_occ_variant_follows_the_swift_declaration(self, scraper: AppleJSONDocumentationScraper) -> None:
        swift = {"kind": "declarations", "declarations": [declaration("func read()")]}
        occ = {"kind": "declarations", "declarations": [declaration("- (void) read;", ["occ"])]}
        json_page = page([swift, content(para("Reads."))], variantOverrides=[{
            "traits": [{"interfaceLanguage": "occ"}],
            "patch": [
                {"op": "replace", "path": "/metadata/title", "value": "read"},
                {"op": "replace", "path": "/metadata/roleHeading", "value": "Instance Method (ObjC)"},
                {"op": "replace", "path": "/metadata/platforms", "value": [{"name": "macOS", "introducedAt": "1.0"}]},
                {"op": "replace", "path": "/primaryContentSections/0", "value": occ},
            ],
        }])
        md = render(scraper, json_page)
        assert "```swift\nfunc read()\n```\n\n```objc\n- (void) read;\n```" in md
        # Everything else stays the Swift page's
        assert md.startswith("# Widget\n\n**Framework**: Test Kit  \n**Kind**: struct  \n**Role**: Structure\n")
        assert "- iOS 17.0+" in md and "macOS 1.0+" not in md
        assert json_page["primaryContentSections"][0] is swift

    def test_occ_patch_without_declarations_adds_nothing(self, scraper: AppleJSONDocumentationScraper) -> None:
        json_page = page([{"kind": "declarations", "declarations": [declaration("func read()")]}],
                         variantOverrides=[{"traits": [{"interfaceLanguage": "occ"}],
                                            "patch": [{"op": "replace", "path": "/references/x/title", "value": "y"}]}])
        md = render(scraper, json_page)
        assert md.count("```") == 2

    @pytest.mark.parametrize("override", [
        # A patch path that doesn't exist
        {"traits": [{"interfaceLanguage": "occ"}],
         "patch": [{"op": "replace", "path": "/primaryContentSections/5", "value": {}}]},
        # A patched declaration whose token has no text
        {"traits": [{"interfaceLanguage": "occ"}],
         "patch": [{"op": "replace", "path": "/primaryContentSections/0", "value": {
             "kind": "declarations", "declarations": [
                 {"languages": ["occ"], "platforms": ["iOS"], "tokens": [{"kind": "text", "text": None}]}]}}]},
        # An operation without a path, an override that isn't one
        {"traits": [{"interfaceLanguage": "occ"}], "patch": [{"op": "replace", "path": None, "value": {}}]},
        "occ",
    ])
    def test_failed_occ_patch_renders_swift_only(
        self, scraper: AppleJSONDocumentationScraper, monkeypatch: pytest.MonkeyPatch, override: Any
    ) -> None:
        warnings = warnings_of(monkeypatch)
        json_page = page([{"kind": "declarations", "declarations": [declaration("func read()")]}],
                         variantOverrides=[override])
        md = render(scraper, json_page)
        assert "## Declaration\n\n```swift\nfunc read()\n```\n\n" in md and md.count("```") == 2
        assert [(w["event"], w["url"]) for w in warnings] == [("occ_variant_patch_failed", URL)]

    def test_occ_override_with_null_traits_or_patch_is_no_variant(
        self, scraper: AppleJSONDocumentationScraper, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        warnings = warnings_of(monkeypatch)
        json_page = page([{"kind": "declarations", "declarations": [declaration("func read()")]}],
                         variantOverrides=[{"traits": None, "patch": []},
                                           {"traits": [{"interfaceLanguage": "occ"}], "patch": None}])
        assert render(scraper, json_page).count("```") == 2
        assert warnings == []

    def test_occ_tag_is_page_wide(self, scraper: AppleJSONDocumentationScraper) -> None:
        def fences(*codes: str) -> str:
            return render(scraper, page([{"kind": "declarations", "declarations": [
                declaration(code, ["occ"], [str(i)]) for i, code in enumerate(codes)]}]))
        assert "```c\nvoid f(int x);" in fences("void f(int x);")
        assert "```objc\n@interface A : NSObject" in fences("@interface A : NSObject")
        assert "```objc\nvoid f(int x);" in fences("void f(int x);", "+ (instancetype) shared;")
        assert "```cpp\nclass A;" in fences("class A;")

    def test_other_overloads(self, scraper: AppleJSONDocumentationScraper) -> None:
        dec = declaration("func title(_ key: String)", otherDeclarations={"displayIndex": 0, "declarations": [
            {"identifier": "doc://x/a", "tokens": tokens("func title(_ text: Text)\n")},
            {"identifier": "doc://x/b", "tokens": tokens("func title<S>(_ s: S)")},
        ]})
        md = render(scraper, page([{"kind": "declarations", "declarations": [dec]}]))
        assert ("```swift\nfunc title(_ key: String)\n```\n\n**Other overloads**:\n\n"
                "```swift\nfunc title(_ text: Text)\n```\n\n```swift\nfunc title<S>(_ s: S)\n```") in md

    def test_conformance_follows_the_declaration(self, scraper: AppleJSONDocumentationScraper) -> None:
        json_page = page([{"kind": "declarations", "declarations": [declaration("func hash(into hasher: inout Hasher)")]}],
                         metadata={"conformance": {
                             "availabilityPrefix": [text("Available when")],
                             "conformancePrefix": [text("Conforms when")],
                             "constraints": [{"type": "codeVoice", "code": "Element"}, text(" conforms to "),
                                             {"type": "codeVoice", "code": "Hashable"}, text(".")]}})
        md = render(scraper, json_page)
        assert "```\n\nAvailable when `Element` conforms to `Hashable`.\n\n" in md


class TestContent:
    def test_headings_use_their_text(self, scraper: AppleJSONDocumentationScraper) -> None:
        md = render(scraper, page([content(
            {"type": "heading", "level": 2, "text": "Return Value", "anchor": "return_value"},
            {"type": "heading", "level": 3, "text": "Review the code structure of a UIKit app", "anchor": "x"},
            {"type": "heading", "level": 3, "anchor": "Set-up-the-docking-region"},
        )]))
        assert "#### Return Value\n" in md
        assert "##### Review the code structure of a UIKit app\n" in md
        # Without text, the anchor (as before)
        assert "##### Set Up the Docking Region" in md

    def test_code_listing_syntax(self, scraper: AppleJSONDocumentationScraper) -> None:
        md = render(scraper, page([content(
            {"type": "codeListing", "syntax": None, "code": ["a = 1"]},
            {"type": "codeListing", "code": ["let b = 2"]},
            {"type": "codeListing", "syntax": "json", "code": ["{}"]},
        )]))
        assert "```\na = 1\n```" in md
        assert "```swift\nlet b = 2\n```" in md
        assert "```json\n{}\n```" in md
        assert "None" not in md

    def test_multi_block_list_items_and_definitions(self, scraper: AppleJSONDocumentationScraper) -> None:
        code = {"type": "codeListing", "syntax": "bash", "code": ["#!/bin/sh", "", "pod install"]}
        md = render(scraper, page([content(
            {"type": "unorderedList", "items": [{"content": [para("One.")]}, {"content": [para("Two."), code]}]},
            {"type": "orderedList", "items": [{"content": [para("Add the script:"), code]}]},
            {"type": "termList", "items": [{"term": {"inlineContent": [text("term")]},
                                            "definition": {"content": [para("First."), para("Second.")]}}]},
        )]))
        assert "- One.\n- Two.\n\n  ```bash\n  #!/bin/sh\n\n  pod install\n  ```" in md
        assert "1. Add the script:\n\n   ```bash\n   #!/bin/sh\n\n   pod install\n   ```" in md
        assert "- **term**: First.\n\n  Second." in md

    @pytest.mark.parametrize("blocks, item, after_label, quote", [
        # A list or code listing alone
        ([LIST], "- - a\n  - b", "\n\n  - a\n  - b", "\n>\n> - a\n> - b"),
        ([CODE], "- ```swift\n  let x = 1\n\n  let y = 2\n  ```", "\n\n  ```swift\n  let x = 1\n\n  let y = 2\n  ```",
         "\n>\n> ```swift\n> let x = 1\n>\n> let y = 2\n> ```"),
        # First among several
        ([LIST, para("After.")], "- - a\n  - b\n\n  After.", "\n\n  - a\n  - b\n\n  After.",
         "\n>\n> - a\n> - b\n>\n> After."),
        ([CODE, para("After.")], "- ```swift\n  let x = 1\n\n  let y = 2\n  ```\n\n  After.",
         "\n\n  ```swift\n  let x = 1\n\n  let y = 2\n  ```\n\n  After.",
         "\n>\n> ```swift\n> let x = 1\n>\n> let y = 2\n> ```\n>\n> After."),
        # After a paragraph: on the label's line, as before
        ([para("Before."), LIST], "- Before.\n\n  - a\n  - b", " Before.\n\n  - a\n  - b", " Before.\n>\n> - a\n> - b"),
    ])
    def test_lists_and_code_never_leave_an_item(
        self, scraper: AppleJSONDocumentationScraper, blocks: List[Dict[str, Any]], item: str, after_label: str,
        quote: str
    ) -> None:
        """Every line of an item's blocks stays in its list item or quote, and a
        list or code listing never follows a label on its line."""
        md = render(scraper, page(
            [content({"type": "unorderedList", "items": [{"content": blocks}, {"content": [para("Next.")]}]},
                     {"type": "orderedList", "items": [{"content": blocks}]},
                     {"type": "termList", "items": [{"term": {"inlineContent": [text("term")]},
                                                     "definition": {"content": blocks}}]},
                     {"type": "aside", "style": "note", "name": "Note", "content": blocks}),
             {"kind": "parameters", "parameters": [{"name": "handler", "content": blocks}]},
             {"kind": "properties", "title": "Properties", "items": [
                 {"name": "status", "type": tokens("string"), "content": blocks}]},
             {"kind": "possibleValues", "title": "Possible Values", "values": [{"name": "on", "content": blocks}]}],
            deprecationSummary=[block for block in blocks if block["type"] != "paragraph"]))
        assert f"\n{item}\n- Next.\n" in md
        assert "\n1. " + item[2:].replace("\n  ", "\n   ") + "\n" in md
        assert f"\n- **term**:{after_label}\n" in md
        assert f"\n> **Note**:{quote}\n" in md
        assert f"\n- `handler`:{after_label}\n" in md
        assert f"\n- `status` (string):{after_label}\n" in md
        assert f"\n- `on`:{after_label}\n" in md
        # The deprecation summary holds only the list or code listing here
        listing = "\n>\n> - a\n> - b" if LIST in blocks else "\n>\n> ```swift\n> let x = 1\n>\n> let y = 2\n> ```"
        assert f"\n> **Deprecated**:{listing}\n" in md

    def test_asides(self, scraper: AppleJSONDocumentationScraper) -> None:
        md = render(scraper, page([content(
            {"type": "aside", "style": "note", "name": "Complexity", "content": [para("O(n).")]},
            {"type": "aside", "style": "note", "name": "Throws", "content": [para("An error.")]},
            {"type": "aside", "style": "warning", "name": "Warning", "content": [para("Careful.")]},
            {"type": "aside", "style": "important", "content": [para("Read this.")]},
            {"type": "aside", "style": "note", "name": "Note", "content": [
                para("Call it:"), {"type": "codeListing", "syntax": "swift", "code": ["try await f()"]}]},
        )]))
        assert "> **Complexity**: O(n)." in md
        assert "> **Throws**: An error." in md
        assert "> ⚠️ **Warning**: Careful." in md
        assert "> ❗ **Important**: Read this." in md
        assert "> **Note**: Call it:\n>\n> ```swift\n> try await f()\n> ```" in md

    def test_rows_links_and_videos(self, scraper: AppleJSONDocumentationScraper) -> None:
        table = {"type": "table", "header": "row", "rows": [[[para("Input")], [para("Type")]], [[para("In")], [para("Float")]]]}
        references = {
            "doc://com.apple.testkit/documentation/TestKit/happybeam": {
                "type": "topic", "kind": "article", "role": "sampleCode", "title": "Happy Beam",
                "url": "/documentation/testkit/happybeam", "abstract": [text("Leverage a Full Space.")]},
            "intro.mp4": {"type": "video", "alt": "A video of the app.", "poster": None, "identifier": "intro.mp4",
                          "variants": [{"traits": ["1x", "dark"], "url": "/videos/com.apple.testkit/intro~dark.mp4"},
                                       {"traits": ["1x", "light"], "url": "/videos/com.apple.testkit/intro.mp4"}]},
        }
        md = render(scraper, page([content(
            {"type": "row", "numberOfColumns": 2, "columns": [{"content": [table], "size": 1}, {"content": [para("Right.")], "size": 1}]},
            {"type": "links", "style": "list", "items": ["doc://com.apple.testkit/documentation/TestKit/happybeam"]},
            {"type": "video", "identifier": "intro.mp4"},
        )], references=references))
        assert "| Input | Type |\n| --- | --- |\n| In | Float |\n\nRight." in md
        assert "- [Happy Beam](./happybeam.md)\n  Leverage a Full Space." in md
        assert "[Video: A video of the app.](https://developer.apple.com/tutorials/videos/com.apple.testkit/intro.mp4)" in md

    def test_unknown_types_render_their_text_and_are_counted(
        self, scraper: AppleJSONDocumentationScraper, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        md = render(scraper, page(
            [content({"type": "small", "inlineContent": [text("Fine print.")]},
                     para("A ", {"type": "newTerm", "inlineContent": [text("term")]}, " and ",
                          {"type": "strikethrough", "inlineContent": [text("old")]}, ".")),
             {"kind": "futureSection", "content": [para("Future text.")]}],
            metadata={"newKey": 1}, futureKey=[]))
        assert "Fine print." in md
        assert "A term and ~~old~~." in md
        assert "Future text." in md
        warnings = warnings_of(monkeypatch)
        render(scraper, page([content({"type": "small", "inlineContent": [text("Again.")]})]))
        scraper._log_unknown_content()
        seen = {(w["what"], w["name"]): w["count"] for w in warnings if w["event"] == "unknown_content"}
        assert seen == {("block type", "small"): 2, ("inline type", "newTerm"): 1, ("section kind", "futureSection"): 1,
                        ("metadata key", "newKey"): 1, ("top-level key", "futureKey"): 1}

    def test_unknown_types_keep_all_their_text(
        self, scraper: AppleJSONDocumentationScraper, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        def example(kind: str, *lines: str) -> Dict[str, Any]:
            return {"type": kind, "syntax": "http", "content": [{"collapsible": False, "code": list(lines)}]}

        md = render(scraper, page([
            content(
                {"type": "dictionaryExample", "summary": [para("A key.")],
                 "example": example("file", "<key>A</key>", "<true/>")},
                {"type": "endpointExample", "summary": [para("Fetch it.")],
                 "request": example("request", "GET /v1/x"), "response": example("response", "HTTP/1.1 200 OK")},
                {"type": "step", "content": [para("Add a view.")], "caption": [para("It appears.")],
                 "media": "view.png", "code": "Sloth-01.swift", "runtimePreview": None},
                para("Call ", {"type": "newCode", "code": "f()"}, " now."),
            ),
            {"kind": "futureSignature", "title": "Signature", "tokens": [
                {"kind": "keyword", "text": "func"}, {"kind": "text", "text": " "}, {"kind": "identifier", "text": "f"}]},
            # Items whose type is tokens, not a type name
            {"kind": "futureItems", "items": [{"name": "state", "type": tokens("string"), "content": [para("The state.")]}]},
        ]))
        assert "A key.\n\n```\n<key>A</key>\n<true/>\n```" in md
        assert "Fetch it.\n\n```\nGET /v1/x\n```\n\n```\nHTTP/1.1 200 OK\n```" in md
        assert "Add a view.\n\nIt appears.\n\n`Sloth-01.swift`" in md
        assert "Call `f()` now." in md
        assert "\nfunc f\n" in md
        assert "\nstring\n\nThe state.\n" in md
        # Identifiers, styles and syntax names aren't text
        for noise in ("view.png", "```http", "\nfile\n", "\nrequest\n", "Signature"):
            assert noise not in md
        warnings = warnings_of(monkeypatch)
        scraper._log_unknown_content()
        assert {(w["what"], w["name"]) for w in warnings} == {
            ("block type", "dictionaryExample"), ("block type", "endpointExample"), ("block type", "step"),
            ("inline type", "newCode"), ("section kind", "futureSignature"), ("section kind", "futureItems")}

    def test_blocks_under_an_unknown_inline_type_stay_on_its_line(self, scraper: AppleJSONDocumentationScraper) -> None:
        """A code listing or list under an unknown inline type is text on its
        paragraph's line: no fence opens (the next paragraph survives) and no
        item leaves the paragraph. A space at its text's end stays."""
        listing = {"type": "codeListing", "syntax": "swift", "code": ["let x = 1", "", "let y = 2"]}
        bullets = {"type": "unorderedList", "items": [{"content": [para("a")]}, {"content": [para("b")]}]}
        md = render(scraper, page([content(
            para("before ", {"type": "mystery", "content": [listing]}, " after"),
            para("NEXT"),
            para("x ", {"type": "mystery", "content": [bullets]}, " y"),
            para("A ", {"type": "mystery", "inlineContent": [text("term ")]}, "and"),
            para("LAST"))]))
        assert ("\nbefore ```swift let x = 1 let y = 2 ``` after\n\nNEXT\n\nx - a - b y\n\nA term and\n\nLAST\n"
                in md)

    def test_known_types_are_the_rendered_ones(
        self, scraper: AppleJSONDocumentationScraper, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        # Every listed type is rendered by its own branch, never by the fallback...
        def no_fallback(*args: Any, **kwargs: Any) -> List[str]:
            raise AssertionError(f"fallback for {args[0]}")

        monkeypatch.setattr(scraper, "_fallback_parts", no_fallback)
        for block_type in KNOWN_BLOCK_TYPES:
            scraper._process_content_items([{"type": block_type}], {})
        for inline_type in KNOWN_INLINE_TYPES:
            scraper._resolve_inline_content([{"type": inline_type}], {})
        assert not scraper._unknown_content

        # ...and every type a branch renders is listed (a type left out would WARN)
        def rendered(method: Any) -> set:
            return set(re.findall(r"item_type == '(\w+)'", inspect.getsource(method)))

        assert rendered(AppleJSONDocumentationScraper._process_content_items) == KNOWN_BLOCK_TYPES
        assert rendered(AppleJSONDocumentationScraper._resolve_inline_content) == KNOWN_INLINE_TYPES

    def test_images(self, scraper: AppleJSONDocumentationScraper) -> None:
        references = {
            "a.png": {"type": "image", "alt": None, "identifier": "a.png", "variants": [
                {"traits": ["2x", "dark"], "url": "/images/com.apple.testkit/a~dark@2x.png"},
                {"traits": ["1x", "light"], "url": "/images/com.apple.testkit/a.png"}]},
            "b.png": {"type": "image", "alt": "A chart.", "identifier": "b.png", "variants": [
                {"traits": ["2x", "light"], "url": "/images/com.apple.testkit/b@2x.png"}]},
        }
        md = render(scraper, page([content(
            para("See ", {"type": "image", "identifier": "a.png"}),
            {"type": "imageBlock", "identifier": "b.png"},
        )], references=references))
        assert "See ![](https://developer.apple.com/tutorials/images/com.apple.testkit/a.png)" in md
        assert "![A chart.](https://developer.apple.com/tutorials/images/com.apple.testkit/b@2x.png)" in md

    def test_an_image_caption_is_under_its_image(self, scraper: AppleJSONDocumentationScraper) -> None:
        references = {
            "b.png": {"type": "image", "alt": "A chart.", "identifier": "b.png", "variants": [
                {"traits": ["2x", "light"], "url": "/images/com.apple.testkit/b@2x.png"}]},
        }
        md = render(scraper, page([content(
            {"type": "imageBlock", "identifier": "b.png", "metadata": {"abstract": [
                {"type": "text", "text": "Sales by\nquarter."}]}},
            para("Next."),
        )], references=references))
        assert "b@2x.png)\nSales by quarter.\n" in md
        assert "\nNext." in md


class TestReferences:
    def test_inline_references(self, scraper: AppleJSONDocumentationScraper) -> None:
        references = {
            "doc://t/documentation/TestKit/Widget/size": topic("size", "/documentation/testkit/widget/size"),
            "doc://t/documentation/TestKit/guide": {"type": "topic", "kind": "article", "role": "article",
                                                    "title": "Using widgets", "url": "/documentation/testkit/guide"},
            "doc://t/documentation/Other": {"type": "topic", "kind": "symbol", "role": "collection",
                                            "title": "Other Kit", "url": "/documentation/other"},
            "doc://t/documentation/BundleResources/aps": topic(
                "APS Environment Entitlement", "/documentation/bundleresources/aps", ideTitle="APS Environment",
                titleStyle="title"),
            "https://www.usb.org/": {"type": "link", "title": "USB-IF", "url": "https://www.usb.org/"},
            "doc://t/__unknown__/Event": {"type": "unresolvable", "title": "Event", "identifier": "doc://t/__unknown__/Event"},
            "doc://t/documentation/TestKit/Key": topic("OSBundleUsageDescriptionKey", "/documentation/testkit/key"),
        }

        def ref(identifier: str, **extra: Any) -> Dict[str, Any]:
            return {"type": "reference", "identifier": identifier, "isActive": True, **extra}

        md = render(scraper, page([content(para(
            ref("doc://t/documentation/TestKit/Widget/size"), " ",
            ref("doc://t/documentation/TestKit/guide"), " ",
            ref("doc://t/documentation/Other"), " ",
            ref("doc://t/documentation/BundleResources/aps"), " ",
            ref("https://www.usb.org/"), " ",
            ref("doc://t/__unknown__/Event"), " ",
            ref("doc://t/documentation/TestKit/Key", overridingTitle="OSBundleUsageDescription",
                overridingTitleInlineContent=[{"type": "codeVoice", "code": "OSBundleUsageDescription"}]),
        ))], references=references))
        assert ("[`size`](./widget/size.md) [Using widgets](./guide.md) "
                "[Other Kit](https://developer.apple.com/documentation/other) "
                "[APS Environment Entitlement](https://developer.apple.com/documentation/bundleresources/aps) "
                "[USB-IF](https://www.usb.org/) Event [`OSBundleUsageDescription`](./key.md)") in md
        assert "comhttps" not in md

    def test_doc_literals_in_text(self, scraper: AppleJSONDocumentationScraper) -> None:
        md = render(scraper, page([content(
            para("See doc://com.apple.documentation/documentation/devicemanagement/status-reports."),
            para("Or doc://com.apple.SwiftUI/documentationSwiftUI/View, and doc://com.apple.metal/metal/mtldevice;"),
            para({"type": "codeVoice", "code": "doc://com.apple.x/documentation/Y"}),
        )]))
        assert "See https://developer.apple.com/documentation/devicemanagement/status-reports." in md
        assert ("Or https://developer.apple.com/documentation/SwiftUI/View, and "
                "https://developer.apple.com/documentation/metal/mtldevice;") in md
        assert "`doc://com.apple.x/documentation/Y`" in md

    def test_topic_like_sections(self, scraper: AppleJSONDocumentationScraper) -> None:
        references = {
            "doc://t/documentation/TestKit/A": topic("A", "/documentation/testkit/a", abstract=[text("The A.")]),
            "doc://t/documentation/TestKit/B": topic("B", "https://example.com/b"),
            "doc://t/documentation/TestKit/A/perform()-1": topic("perform()", "/documentation/testkit/a/perform()-1"),
            "doc://t/__unknown__/Event": {"type": "unresolvable", "title": "Event", "identifier": "doc://t/__unknown__/Event"},
            "doc://t/documentation/TestKit/M": {"type": "topic", "kind": "article", "role": "article", "title": "M"},
        }
        json_page = page(
            [{"kind": "mentions", "mentions": ["doc://t/documentation/TestKit/M"]}],
            references=references,
            topicSections=[{"title": "Types", "identifiers": ["doc://t/documentation/TestKit/A"]}],
            defaultImplementationsSections=[{"title": "A Implementations", "anchor": "x",
                                             "identifiers": ["doc://t/documentation/TestKit/A/perform()-1"]}],
            seeAlsoSections=[{"title": "Related", "identifiers": ["doc://t/documentation/TestKit/B"]},
                             {"title": "More", "identifiers": ["doc://t/documentation/TestKit/A"]}],
            relationshipsSections=[{"title": "Inherits From", "type": "inheritsFrom", "identifiers": ["doc://t/__unknown__/Event"]}],
        )
        md = render(scraper, json_page)
        assert "## Mentions\n\n- M\n" in md
        assert ("## Topics\n\n### Types\n- [A](./a.md)\n  The A.\n\n"
                "## Default Implementations\n\n### A Implementations\n- [perform()](./a/perform%28%29-1.md)") in md
        assert "## Relationships\n\n### Inherits From\n- Event\n" in md
        assert "## See Also\n\n### Related\n- [B](https://example.com/b)\n### More\n- [A](./a.md)\n  The A." in md


class TestMetadataAndAvailability:
    def test_header_lines(self, scraper: AppleJSONDocumentationScraper) -> None:
        json_page = page(metadata={"required": True}, sampleCodeDownload={
            "kind": "sampleDownload", "action": {"identifier": "55e1/Hello.zip", "isActive": True,
                                                  "overridingTitle": "Download", "type": "reference"}},
            references={"55e1/Hello.zip": {"type": "download", "identifier": "55e1/Hello.zip", "url": "55e1/Hello.zip"}})
        md = render(scraper, json_page)
        assert md.startswith(
            "# Widget\n\n**Framework**: Test Kit  \n**Kind**: struct  \n**Role**: Structure  \n**Required**: Yes  \n"
            "**Download**: [Hello.zip](https://docs-assets.developer.apple.com/published/55e1/Hello.zip)\n\n")

    def test_a_page_without_role_heading_has_no_role_line(self, scraper: AppleJSONDocumentationScraper) -> None:
        md = render(scraper, page(metadata={"symbolKind": None, "roleHeading": None}))
        assert md.startswith("# Widget\n\n**Framework**: Test Kit\n\n")

    def test_availability_and_deprecation(self, scraper: AppleJSONDocumentationScraper) -> None:
        json_page = page(
            [{"kind": "declarations", "declarations": [declaration("var back: Orientation")]}],
            abstract=[text("The back.")],
            metadata={"platforms": [
                {"name": "iOS", "introducedAt": "7.0", "deprecated": True, "renamed": "Orientation.back"},
                {"name": "macOS", "introducedAt": "10.0", "deprecatedAt": "27.0", "message": "Use another API."},
                {"name": "visionOS", "deprecated": True, "message": "Use another API."},
                {"name": "watchOS", "introducedAt": "2.0", "beta": True},
            ]})
        md = render(scraper, json_page)
        assert ("The back.\n\n**Availability**:\n"
                "- iOS 7.0+ - Deprecated (renamed: Orientation.back)\n"
                "- macOS 10.0+ - Deprecated in 27.0\n"
                "- visionOS - Deprecated\n"
                "- watchOS 2.0+ (Beta)\n\n"
                "> **Deprecated**: Use another API.\n\n## Declaration") in md
        assert "?+" not in md

    def test_deprecation_summary_wins_over_messages(self, scraper: AppleJSONDocumentationScraper) -> None:
        json_page = page(
            deprecationSummary=[para("Use ", {"type": "codeVoice", "code": "new()"}, "."), para("Not this.")],
            metadata={"platforms": [{"name": "iOS", "introducedAt": "7.0", "deprecatedAt": "13.0", "message": "Old."}]})
        md = render(scraper, json_page)
        assert "- iOS 7.0+ - Deprecated in 13.0\n\n> **Deprecated**: Use `new()`. Not this.\n" in md
        assert "Old." not in md


class TestRestAndKeys:
    def test_rest_endpoint(self, scraper: AppleJSONDocumentationScraper) -> None:
        item = {"name": "id", "required": True, "type": tokens("string"), "content": [para("The ID.")]}
        query = {"name": "limit", "type": tokens("integer"), "content": [para("The count.")],
                 "attributes": [{"kind": "default", "value": "5"}, {"kind": "maximum", "value": "25"}]}
        old = {"name": "fields", "deprecated": True, "type": tokens("[string]"), "content": []}
        json_page = page([
            {"kind": "restEndpoint", "title": "URL", "tokens": tokens("GET https://api.example.com/v1/{id}")},
            {"kind": "restParameters", "source": "path", "title": "Path Parameters", "items": [item]},
            {"kind": "restParameters", "source": "query", "title": "Query Parameters", "items": [query, old]},
            {"kind": "restBody", "title": "HTTP Body", "mimeType": "application/json", "parameters": [],
             "bodyContentType": tokens("WidgetRequest"), "content": [para("The request.")]},
            {"kind": "restResponses", "title": "Response Codes", "items": [
                {"status": 200, "reason": "OK", "mimeType": "application/json", "type": tokens("WidgetResponse"),
                 "content": [para("Succeeded.")]},
                {"status": 429, "type": [], "content": [para("")]},
            ]},
        ], metadata={"symbolKind": "httpRequest", "roleHeading": "Web Service Endpoint"})
        md = render(scraper, json_page)
        assert ("## Parameters\n\n### Path Parameters\n\n- `id` (string) *(required)*: The ID.\n\n"
                "### Query Parameters\n\n- `limit` (integer): The count.\n\n  **Default**: `5`; **Maximum**: `25`\n"
                "- `fields` ([string]) *(deprecated)*\n\n") in md
        assert ("## Request Body\n\n**Content-Type**: `application/json`  \n**Type**: `WidgetRequest`\n\n"
                "The request.\n\n") in md
        assert ("## Responses\n\n- `200` OK (`WidgetResponse`, `application/json`): Succeeded.\n- `429`\n") in md

    def test_property_attributes(self, scraper: AppleJSONDocumentationScraper) -> None:
        json_page = page([{"kind": "properties", "title": "Properties", "items": [
            {"name": "errorCode", "required": True, "type": tokens("int64"), "content": [],
             "attributes": [{"kind": "allowedValues", "values": ["4000127"]}]},
            {"name": "status", "type": tokens("string"), "content": [
                para("One of:"), {"type": "unorderedList", "items": [{"content": [para("`a`")]}]}],
             "attributes": [{"kind": "allowedValues", "values": ["a"]}]},
        ]}])
        md = render(scraper, json_page)
        assert "- `errorCode` (int64) *(required)*: **Allowed Values**: `4000127`\n" in md
        assert "- `status` (string): One of:\n\n  - `a`\n\n  **Allowed Values**: `a`" in md

    def test_details_and_possible_values_follow_the_declaration(self, scraper: AppleJSONDocumentationScraper) -> None:
        json_page = page([
            {"kind": "details", "title": "Details", "details": {
                "name": "aps-environment", "ideTitle": "APS Environment", "titleStyle": "title", "platforms": [],
                "value": [{"arrayMode": False, "baseType": "string"}]}},
            {"kind": "possibleValues", "title": "Possible Values", "values": [
                {"name": "development", "content": [para("The development environment.")]},
                {"name": "production", "content": [para("The production environment.")]}]},
            content({"type": "heading", "level": 2, "text": "Discussion", "anchor": "Discussion"}, para("Text.")),
        ], metadata={"title": "APS Environment Entitlement", "roleHeading": "Property List Key"})
        md = render(scraper, json_page)
        assert ("- iOS 17.0+\n\n## Details\n\n- **Name**: `aps-environment` (APS Environment)\n- **Type**: string\n\n"
                "## Possible Values\n\n- `development`: The development environment.\n"
                "- `production`: The production environment.\n\n#### Discussion") in md
        same = page([{"kind": "details", "title": "Details", "details": {
            "name": "NSFoo", "ideTitle": "Foo", "value": [{"arrayMode": True, "baseType": "string"}]}}],
            metadata={"title": "Foo"})
        assert "- **Name**: `NSFoo`\n- **Type**: array of string" in render(scraper, same)

    def test_parameter_descriptions_keep_later_blocks(self, scraper: AppleJSONDocumentationScraper) -> None:
        json_page = page([{"kind": "parameters", "parameters": [
            {"name": "handler", "content": [para("Called once."), para("On the main queue.")]}]}])
        assert "## Parameters\n\n- `handler`: Called once.\n\n  On the main queue." in render(scraper, json_page)
