#!/usr/bin/env python3
"""Unit tests for metadata extractor."""

import unittest
import tempfile
import os
from pathlib import Path
from metadata_extractor import MetadataExtractor

class TestMetadataExtractor(unittest.TestCase):
    """Test metadata extraction functionality."""
    
    def setUp(self):
        self.extractor = MetadataExtractor()
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        import shutil
        shutil.rmtree(self.test_dir)
    
    def create_test_file(self, content: str, path: str = "test.md") -> str:
        """Create a test markdown file."""
        file_path = os.path.join(self.test_dir, path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            f.write(content)
        return file_path
    
    def test_extract_api_name(self):
        """Test API name extraction: the base name of the H1."""
        test_cases = [
            ("# UIView\n\nA view class", "UIView"),
            ("# init(viewControllerProvider:)\n\n**Kind**: init", "init"),
            ("# callAsFunction()\n", "callAsFunction"),
            ("# ==(_:_:)\n", "=="),
            ("# .<=(_:_:)\n", ".<="),
            ("# Transaction.AdvancedCommerceInfo\n", "AdvancedCommerceInfo"),
            ("# EntitlementTaskState.failure(_:)\n", "failure"),
            ("# IOHIDInterface::InterruptReportAction\n", "InterruptReportAction"),
            ("# mlx.core.array\n", "array"),
            # Not a symbol name: the whole title
            ("# Foundation Models\n\n**Kind**: module", "Foundation Models"),
            ("# Vector3 (Half)\n", "Vector3 (Half)"),
            ("# Declaring a custom view\n", "Declaring a custom view"),
            ("# tvOS 17.5 Release Notes\n", "tvOS 17.5 Release Notes"),
        ]
        
        for content, expected in test_cases:
            with self.subTest(content=content):
                result = self.extractor.extract_api_name(content, "test.md")
                self.assertEqual(result, expected)

    def test_extract_api_name_ignores_names_in_code_and_prose(self) -> None:
        """A declaration or sample code naming another type doesn't become the API name."""
        content = """# isResponding

**Framework**: Foundation Models  
**Kind**: property

A Boolean value that indicates a response is being generated.

```swift
struct ShopView: View {
    var session: LanguageModelSession
}
```
"""
        self.assertEqual(self.extractor.extract_api_name(content, "documentation/FoundationModels/isresponding.md"),
                         "isResponding")
        # No title: the file name
        self.assertEqual(self.extractor.extract_api_name("class MyCustomView {}", "docs/MyCustomView.md"),
                         "MyCustomView")
    
    def test_extract_api_name_of_dotted_titles(self) -> None:
        """A nested symbol's qualifier is dropped; a dotted name that is the page's own is kept."""
        def apple(title: str, kind: str, url: str) -> str:
            kind_line = f"  \n**Kind**: {kind}" if kind else ""
            return (f"# {title}\n\n**Framework**: Kit{kind_line}\n\nA summary.\n\n---\n\n"
                    f"*[View on Apple Developer](https://developer.apple.com/documentation/{url})*\n")
        test_cases = [
            # Apple nests a nested symbol under its parent's page
            (apple("Accessory.Chirality", "enum", "arkit/accessory/chirality"), "Chirality"),
            (apple("Accessory.Source", "enum", "arkit/accessory/source-swift.enum"), "Source"),
            (apple("TossableRepresentation.OctahedronFace.h", "case",
                   "tabletopkit/tossablerepresentation/octahedronface/h"), "h"),
            (apple("IOHIDInterface::CompletionAction", "tdef",
                   "kernel/iohidinterface/iohidinterface_completionaction"), "CompletionAction"),
            # An article (no **Kind** line): a header file's name
            (apple("AXError.h", "", "applicationservices/axerror-h"), "AXError.h"),
            # A page its URL names by the whole title: a property list key, a JS class
            (apple("com.apple.security.network.client", "typealias",
                   "bundleresources/entitlements/com.apple.security.network.client"),
             "com.apple.security.network.client"),
            (apple("CloudKit.Database", "class", "cloudkitjs/cloudkit.database"), "CloudKit.Database"),
            # Other sources: a qualified API name
            ("---\nsource: MLX\nframework: MLX\nurl: https://ml-explore.github.io/mlx/build/html/python/"
             "_autosummary/mlx.core.array.diag.html\n---\n\n# mlx.core.array.diag\n", "diag"),
        ]
        for content, expected in test_cases:
            with self.subTest(content=content):
                self.assertEqual(self.extractor.extract_api_name(content, "test.md"), expected)

    def test_extract_framework(self):
        """Test framework extraction."""
        # Test path-based extraction
        path = "documentation/SwiftUI/View.md"
        result = self.extractor.extract_framework("", path)
        self.assertEqual(result, "SwiftUI")
        
        # Test content-based extraction
        content = "Framework: UIKit\n\nSome content"
        result = self.extractor.extract_framework(content, "test.md")
        self.assertEqual(result, "UIKit")
        
        # Test import-based extraction
        content = "import Foundation\n\nclass MyClass {}"
        result = self.extractor.extract_framework(content, "test.md")
        self.assertEqual(result, "Foundation")
    
    def test_extract_platforms(self):
        """Test platform extraction."""
        test_cases = [
            ("Available on: iOS 15+, macOS 12+", ["iOS", "macOS"]),
            ("Platforms: iOS, tvOS, watchOS", ["iOS", "tvOS", "watchOS"]),
            ("@available(iOS 14, macOS 11, *)", ["iOS", "macOS"]),
            ("![iOS](badge-ios.png) ![macOS](badge-macos.png)", ["iOS", "macOS"]),
            ("`iOS 15.0+` `macOS 12.0+` `Mac Catalyst 15.0+`", ["Mac Catalyst", "iOS", "macOS"]),
        ]
        
        for content, expected in test_cases:
            with self.subTest(content=content):
                result = self.extractor.extract_platforms(content)
                self.assertEqual(sorted(result), sorted(expected))
    
    def test_extract_platforms_from_availability(self) -> None:
        """Apple pages: the **Availability** list, whatever the text mentions."""
        content = """# IOServiceOpen(_:_:_:_:)

**Framework**: IOKit  
**Kind**: func

Creates a connection to the IOService. See IOSurface for iOS-style surfaces.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.0+ - Deprecated in 12.0: Use the renamed API
- visionOS ?+
- tvOS 18.0+ (Beta)
- DriverKit 19.0+

## Declaration
"""
        self.assertEqual(self.extractor.extract_platforms(content), ["Mac Catalyst", "macOS", "tvOS", "visionOS"])

    def test_availability_grammar_is_tolerant(self) -> None:
        """Every item form the converter writes, and the legacy "?+" version."""
        items = [
            ("- iOS 13.0+", "iOS"),
            ("- iPadOS 13.0+ (Beta)", "iPadOS"),
            ("- macOS ?+", "macOS"),
            ("- watchOS", "watchOS"),
            ("- tvOS 9.0+ - Deprecated", "tvOS"),
            ("- Mac Catalyst 13.1+ - Deprecated in 17.0", "Mac Catalyst"),
            ("- visionOS 1.0+ (Beta) - Deprecated in 2.0: Use `other(_:)` instead.", "visionOS"),
            ("- iOS 2.0+ - Deprecated in 8.0 (renamed: newName(_:))", "iOS"),
            # The converter's bare platform (no introduced version) and renamed-only forms
            ("- visionOS - Deprecated", "visionOS"),
            ("- macOS (Beta)", "macOS"),
            ("- iOS 7.0+ - Deprecated (renamed: AVAudioSession.Orientation.back)", "iOS"),
        ]
        for item, expected in items:
            with self.subTest(item=item):
                content = f"# x\n\n**Availability**:\n{item}\n\n## Declaration\n"
                self.assertEqual(self.extractor.extract_platforms(content), [expected])

    def test_availability_without_an_os_platform_lists_none(self) -> None:
        """A page available only outside the OS platforms (a web service, Xcode) has none."""
        content = "# Get an App\n\nUse it from iOS apps.\n\n**Availability**:\n- App Store Connect API 1.0+\n"
        self.assertEqual(self.extractor.extract_platforms(content), [])

    def test_extract_deprecated(self) -> None:
        """Deprecated: Apple's summary before the page's first section, or every listed platform."""
        summary = ("# scheduleLocalNotification(_:)\n\n**Framework**: UIKit  \n**Kind**: method\n\n"
                   "Schedules a local notification.\n\n**Availability**:\n- iOS 4.0+ - Deprecated in 10.0\n\n"
                   "> **Deprecated**: Use the [`UNUserNotificationCenter`](../x.md) class instead.\n\n"
                   "## Declaration\n")
        cases = [
            (summary, True),
            # Every platform deprecated, without a summary
            ("# a\n\n**Availability**:\n- iOS 2.0+ - Deprecated in 8.0\n- macOS 10.5+ - Deprecated\n\n"
             "## Declaration\n", True),
            # Apple's page-level summary on a page one platform still lists as current
            ("# a\n\n**Availability**:\n- iOS 15.0+\n- macOS 12.0+ - Deprecated in 14.0\n\n"
             "> **Deprecated**: Use `b` instead.\n\n## Declaration\n", True),
            # Deprecated on some platforms only, without a summary
            ("# a\n\n**Availability**:\n- iOS 15.0+\n- macOS 12.0+ - Deprecated in 14.0\n\n## Declaration\n", False),
            ("# a\n\n**Availability**:\n- iOS 15.0+\n\n## Declaration\n", False),
            ("# Scheduling a notification\n\n**Framework**: User Notifications\n\nCreate one.\n\n#### Overview\n\nText.\n",
             False),
            # A quote or a list in a later section isn't the page's
            ("# a\n\n**Availability**:\n- iOS 15.0+\n\n## Discussion\n\n> **Deprecated**: quoted in the text\n", False),
            ("# a\n\n## Topics\n\n**Availability**:\n- iOS 2.0+ - Deprecated\n", False),
        ]
        for content, expected in cases:
            with self.subTest(content=content[:60]):
                self.assertIs(self.extractor.extract_deprecated(content), expected)
        self.assertIs(self.extractor.extract_metadata(summary, "documentation/UIKit/a.md")["deprecated"], True)
        self.assertIs(self.extractor.extract_metadata(cases[3][0], "documentation/UIKit/b.md")["deprecated"], False)

    def test_extract_deprecation(self) -> None:
        """The deprecation summary's first paragraph, on one line; none without a summary (or
        after a section)."""
        content = ("# a\n\n**Availability**:\n- iOS 2.0+ - Deprecated\n\n"
                   "> **Deprecated**: Use [`b`](./b.md)\n> instead.\n\n## Declaration\n")
        self.assertEqual(self.extractor.extract_deprecation(content), "Use [`b`](./b.md) instead.")
        self.assertEqual(self.extractor.extract_metadata(content, "documentation/UIKit/a.md")["deprecation"],
                         "Use [`b`](./b.md) instead.")
        # Its later blocks aren't what to use instead: a code sample, a stray heading of Apple's
        for rest in ("> ```swift\n> let x = try b()\n> ```\n", "> #### Discussion\n"):
            with self.subTest(rest=rest):
                quote = f"# a\n\n> **Deprecated**: Use `b` instead.\n>\n{rest}\n## Declaration\n"
                self.assertEqual(self.extractor.extract_deprecation(quote), "Use `b` instead.")
        for content in ("# a\n\n**Availability**:\n- iOS 2.0+ - Deprecated\n\n## Declaration\n",
                        "# a\n\n## Discussion\n\n> **Deprecated**: quoted in the text\n"):
            with self.subTest(content=content[:40]):
                self.assertIsNone(self.extractor.extract_deprecation(content))
                self.assertNotIn("deprecation", self.extractor.extract_metadata(content, "documentation/UIKit/a.md"))

    def test_platform_scan_matches_whole_words_only(self) -> None:
        """Without an Availability list, IOService or IOSurface don't name iOS."""
        self.assertEqual(self.extractor.extract_platforms("Registers an IOService with the IOSurface."), [])
        self.assertEqual(self.extractor.extract_platforms("Uses AVAudioSession in scenarios like UPL_IOSYNC."), [])
        self.assertEqual(self.extractor.extract_platforms("Supported on iOS and iPadOS devices."), ["iOS", "iPadOS"])
        # A version right after the name
        self.assertEqual(self.extractor.extract_platforms("Deployable on iOS15+ and tvOS15+ (ct.target.macOS13)."),
                         ["iOS", "macOS", "tvOS"])
    
    def test_extract_kind(self):
        """Test API kind extraction: the **Kind** line, normalized."""
        test_cases = [
            ("class", "class"),
            ("cl", "class"),
            ("struct", "struct"),
            ("protocol", "protocol"),
            ("intf", "protocol"),
            ("enum", "enum"),
            ("method", "method"),
            ("instm", "method"),
            ("clm", "method"),
            ("func", "function"),
            ("init", "init"),
            ("structctr", "init"),
            ("property", "property"),
            ("structp", "property"),
            ("var", "variable"),
            ("data", "variable"),
            ("case", "case"),
            ("econst", "case"),
            ("tdef", "typealias"),
            ("op", "operator"),
            ("httpRequest", "endpoint"),
            ("dictionary", "object"),
            ("module", "module"),
            ("uid", "unknown"),
            ("somethingNew", "unknown"),
        ]
        
        for raw, expected in test_cases:
            with self.subTest(raw=raw):
                content = f"# Name\n\n**Framework**: Kit  \n**Kind**: {raw}\n\nA summary.\n"
                result = self.extractor.extract_kind(content)
                self.assertEqual(result, expected)

    def test_extract_kind_without_a_kind_line(self) -> None:
        """No **Kind** line: the kind its **Role** line names (ROLE_KINDS), else an article,
        whatever its code shows."""
        test_cases = [
            "# Declaring a custom view\n\n**Framework**: SwiftUI\n\n```swift\nstruct MyView: View {}\n```\n",
            "# Declaring a custom view\n\n**Framework**: SwiftUI  \n**Role**: Article\n\nText.\n",
            "class MyView: UIView {",
            "func calculate() -> Int",
            # A **Kind** line further down is not the page's header
            "# Title\n\nSome text.\n\n**Kind**: class\n",
            # Nor a **Role** line
            "# Title\n\nSome text.\n\n**Role**: Sample Code\n",
            # A role the table doesn't list
            "# Release Notes\n\n**Framework**: Xcode  \n**Role**: Release Notes\n",
            # The HIG's header
            "---\nurl: https://example.com\n---\n\n# Images\n\n**Type:** article\n\n**Platforms:** ios, macos\n",
        ]
        for content in test_cases:
            with self.subTest(content=content):
                self.assertEqual(self.extractor.extract_kind(content), "article")
        roles = [("API Collection", "collection"), ("Sample Code", "sample-code"), ("Article", "article")]
        for role, expected in roles:
            with self.subTest(role=role):
                content = (f"# Title\n\n**Framework**: Kit  \n**Role**: {role}  \n"
                           "**Download**: [App.zip](https://docs-assets.developer.apple.com/published/1/App.zip)\n\nText.\n")
                self.assertEqual(self.extractor.extract_kind(content), expected)
        # The **Kind** line keeps priority
        framework = "# Kit\n\n**Framework**: Kit  \n**Kind**: module  \n**Role**: Framework\n\nText.\n"
        self.assertEqual(self.extractor.extract_kind(framework), "module")
        method = "# f()\n\n**Framework**: Kit  \n**Kind**: method  \n**Role**: Instance Method\n\nText.\n"
        self.assertEqual(self.extractor.extract_kind(method), "method")
    
    def test_extract_overview(self):
        """Test overview extraction."""
        content = """
# MyClass

## Overview

This is a comprehensive overview that explains what MyClass does.
It can span multiple lines and provides detailed information.

## Usage

Here's how to use it.
"""
        result = self.extractor.extract_overview(content)
        self.assertIn("comprehensive overview", result)
        self.assertIn("MyClass", result)
        self.assertNotIn("Usage", result)
    
    def test_extract_overview_is_never_cut_inside_a_link(self) -> None:
        """An overview over 500 characters is cut before a link the cut would fall in, at 500
        characters otherwise."""
        link = "[`updatePostbackConversionValue(_:coarseValue:)`](./skadnetwork/updatepostback%28_,coarsevalue%29.md)"
        content = "# A\n\n## Overview\n\n" + "x" * 480 + " See " + link + " for more.\n"
        self.assertEqual(self.extractor.extract_overview(content), "x" * 480 + " See")
        # A link with parentheses in its URL, and an image
        for link in ("[frame](https://developer.apple.com/documentation/swiftui/view/frame(width:height:))",
                     "![Diagram](https://h.test/diagram.png)"):
            self.assertEqual(self.extractor.extract_overview("# A\n\n" + "y" * 495 + " " + link + "\n"), "y" * 495)
        # One that ends before the cut stays whole
        content = "# A\n\n[B](b.md) " + "z" * 600 + "\n"
        self.assertEqual(self.extractor.extract_overview(content), "[B](b.md) " + "z" * 490)

    def test_extract_overview_skips_header_lines(self) -> None:
        """Without an Overview section: the abstract, not the header's **Key**: value lines."""
        apple = """# isResponding

**Framework**: Foundation Models  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates a response is being generated.

**Availability**:
- iOS 26.0+
"""
        self.assertEqual(self.extractor.extract_overview(apple),
                         "A Boolean value that indicates a response is being generated.")
        # No abstract: nothing from the header or the Availability list
        bare = ("# v1\n\n**Framework**: Kernel  \n**Kind**: unionp\n\n**Availability**:\n- macOS 10.13.4+\n\n"
                "## Declaration\n\n```swift\nIOFBHDRMetaDataV1 v1;\n```\n")
        self.assertEqual(self.extractor.extract_overview(bare), "")
        # Nothing but the header and the footer: not the footer's rule
        footer_only = ("# kSomeConstant\n\n**Framework**: Kernel  \n**Kind**: econst\n\n---\n\n"
                       "*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ksomeconstant)*\n")
        self.assertEqual(self.extractor.extract_overview(footer_only), "")
        # The HIG's "**Key:** value" header
        hig = ("---\nurl: https://example.com\n---\n\n# Images\n\n**Type:** article\n\n"
               "**Platforms:** ios, macos\n\nImages convey meaning.\n")
        self.assertEqual(self.extractor.extract_overview(hig), "Images convey meaning.")
        # A symbol titled "description": its title isn't an Overview section heading
        titled = "# description\n\n**Framework**: ARKit  \n**Kind**: property\n\nA textual representation.\n"
        self.assertEqual(self.extractor.extract_overview(titled), "A textual representation.")

    def test_extract_overview_skips_the_deprecation_summary(self) -> None:
        """The deprecation summary after the Availability list is no overview: without an
        abstract the page has none; with one, the abstract."""
        bare = ("# CKContainer_Application_PermissionBlock\n\n**Framework**: CloudKit  \n**Kind**: typealias  \n"
                "**Role**: Type Alias\n\n**Availability**:\n- iOS 8.0+ - Deprecated\n- visionOS - Deprecated\n\n"
                "> **Deprecated**: renamed to CKContainer.ApplicationPermissionBlock\n>\n> ```swift\n> old()\n> ```\n\n"
                "## Declaration\n\n```swift\ntypealias CKContainer_Application_PermissionBlock = X\n```\n")
        self.assertEqual(self.extractor.extract_overview(bare), "")
        no_availability = ("# old\n\n**Framework**: Kit  \n**Kind**: func\n\n> **Deprecated**: Use new().\n\n"
                           "Some text after it.\n")
        self.assertEqual(self.extractor.extract_overview(no_availability), "Some text after it.")
        abstract = ("# old\n\n**Framework**: Kit  \n**Kind**: func  \n**Role**: Function\n\nDoes the old thing.\n\n"
                    "**Availability**:\n- macOS 10.0+ - Deprecated in 13.0\n\n> **Deprecated**: Use new().\n")
        self.assertEqual(self.extractor.extract_overview(abstract), "Does the old thing.")

    def test_extract_overview_skips_any_leading_quote(self) -> None:
        """Any quote before the page's first paragraph is a banner, not its summary: the
        HIG's "Updated" note (108 pages' summary until PROCESSOR_VERSION 5), a GitHub
        admonition, a guide's "Part of" note. A page with no paragraph after it takes the
        first banner's text, without its markup (a deprecation summary is never one); a
        quote after the first paragraph is text."""
        hig = ("---\nurl: https://developer.apple.com/design/human-interface-guidelines/buttons\n---\n\n"
               "# Buttons\n\n**Type:** article\n\n**Platforms:** ios, macos\n\n"
               "> **Updated 2025-12-16:** Updated guidance for Liquid Glass.\n\n"
               "A button initiates an instantaneous action.\n\n## Best practices\n")
        self.assertEqual(self.extractor.extract_overview(hig), "A button initiates an instantaneous action.")
        admonition = ("---\nsource: container\n---\n\n# How-to\n\n> [!IMPORTANT]\n"
                      "> This file contains documentation for the CURRENT BRANCH.\n\n"
                      "How to use the features of `container`.\n")
        self.assertEqual(self.extractor.extract_overview(admonition), "How to use the features of `container`.")
        note = "# Guide\n\n**Framework**: Kit\n\n> **Note**: Read this first.\n"
        self.assertEqual(self.extractor.extract_overview(note), "Read this first.")
        banner_only = ("# Buttons\n\n> **Updated 2025-12-16:** Updated guidance for Liquid Glass.\n\n"
                       "## Best practices\n\nUse a button.\n")
        self.assertEqual(self.extractor.extract_overview(banner_only), "Updated guidance for Liquid Glass.")
        important = "# How-to\n\n> [!IMPORTANT]\n> Read the release notes.\n>\n> More.\n\n> Second quote.\n"
        self.assertEqual(self.extractor.extract_overview(important), "Read the release notes.")
        deprecated_then_note = ("# old\n\n> **Deprecated**: Use new().\n\n> **Note:** Kept for old apps.\n\n"
                                "## Declaration\n")
        self.assertEqual(self.extractor.extract_overview(deprecated_then_note), "Kept for old apps.")
        later = "# Guide\n\nThe guide.\n\n> **Note**: Read this first.\n"
        self.assertEqual(self.extractor.extract_overview(later), "The guide.")

    def test_extract_overview_section_skips_rules_and_labels(self) -> None:
        """An Overview section's rule, lone "**Label**:" line or footer is no overview."""
        footer = "\n\n---\n\n*[View on Apple Developer](https://developer.apple.com/documentation/kit/x)*\n"
        # A rule before the abstract
        ruled = ("# PHASEStreamNode\n\n**Framework**: PHASE  \n**Kind**: class\n\n## Declaration\n\n"
                 "```swift\nclass PHASEStreamNode\n```\n\n#### Overview\n\n---\n\n"
                 "The base class for stream nodes.\n\n## Topics\n" + footer)
        self.assertEqual(self.extractor.extract_overview(ruled), "The base class for stream nodes.")
        # An empty section, then the footer: no abstract at all
        empty = "# gKey\n\n**Framework**: Kernel  \n**Kind**: data\n\n#### Overview\n" + footer
        self.assertEqual(self.extractor.extract_overview(empty), "")
        # A label heading a code block: the page's abstract instead
        labeled = ("# attributedString\n\n**Framework**: UIKit\n\nThe text storage object.\n\n#### Overview\n\n"
                   "**Swift**:\n\n```swift\nvar attributedString: NSAttributedString? { get }\n```\n\n"
                   "This property is part of the protocol.\n" + footer)
        self.assertEqual(self.extractor.extract_overview(labeled), "The text storage object.")
        # A rule, then a second Overview section
        twice = ("# Xcode 12.4 Release Notes\n\nUpdate your apps.\n\n#### Overview\n\n---\n\n#### Overview\n\n"
                 "Xcode 12.4 includes SDKs for iOS 14.4.\n" + footer)
        self.assertEqual(self.extractor.extract_overview(twice), "Xcode 12.4 includes SDKs for iOS 14.4.")
        # A "#" inside the paragraph (a link's fragment) is no heading
        linked = ("# ParameterSummary\n\n## Overview\n\nFor more, see [`Summaries`](intents#Provide-a-summary) "
                  "and the  #if  directive.\nSecond line.\n\n## Topics\n")
        self.assertEqual(self.extractor.extract_overview(linked),
                         "For more, see [`Summaries`](intents#Provide-a-summary) and the #if directive. Second line.")
        # A paragraph without a letter or digit: the abstract instead, or nothing
        stray = ("# CapturedRoom.AttributesCodableRepresentation\n\n**Framework**: RoomPlan  \n**Kind**: struct\n\n"
                 "A serializable set of details.\n\n#### Overview\n\n}\n\n## Topics\n" + footer)
        self.assertEqual(self.extractor.extract_overview(stray), "A serializable set of details.")
        sphinx = "---\nurl: https://example.com/a.html\n---\n\n# mlx.core.diag\n\n**\n\n- [.rst](a.rst)\n"
        self.assertEqual(self.extractor.extract_overview(sphinx), "")

    def test_framework_normalization(self):
        """Test framework name normalization."""
        test_cases = [
            ("swiftui", "SwiftUI"),
            ("swift ui", "SwiftUI"),
            ("uikit", "UIKit"),
            ("coredata", "CoreData"),
            ("core data", "CoreData"),
            ("CustomFramework", "CustomFramework"),  # Unknown framework
        ]
        
        for input_name, expected in test_cases:
            with self.subTest(input=input_name):
                result = self.extractor.normalize_framework_name(input_name)
                self.assertEqual(result, expected)
    
    def test_document_id_generation(self):
        """Test document ID generation: the SHA-1 of the file_path."""
        import hashlib
        test_cases = [
            ("documentation/SwiftUI/View.md", "documentation/SwiftUI/View.md"),
            ("/app/documentation/UIKit/UIViewController.md", "documentation/UIKit/UIViewController.md"),
            ("documentation/Core-Data/NSManagedObject.md", "documentation/Core-Data/NSManagedObject.md"),
        ]
        
        for path, file_path in test_cases:
            with self.subTest(path=path):
                result = self.extractor.generate_document_id(path)
                self.assertEqual(result, hashlib.sha1(file_path.encode("utf-8")).hexdigest())
                self.assertRegex(result, r"^[0-9a-f]{40}$")

    def test_document_ids_differ_where_legacy_ids_collided(self) -> None:
        """Paths that differ only in case or punctuation get different ids."""
        paths = [
            "documentation/Swift/Int/init(_:).md",
            "documentation/Swift/Int/init-_-.md",
            "documentation/Swift/int/init(_:).md",
            "documentation/Swift/Int/INIT(_:).md",
        ]
        ids = {self.extractor.generate_document_id(p) for p in paths}
        self.assertEqual(len(ids), len(paths))
        # A file name that isn't valid UTF-8 (Linux) still gets an id
        self.assertRegex(self.extractor.generate_document_id("documentation/Zz/a\udcff.md"), r"^[0-9a-f]{40}$")
    
    def test_file_path_and_id_outside_a_documentation_dir(self) -> None:
        """Without a documentation dir in the path: the whole path, so same-named files stay apart."""
        paths = ["/tmp/docs/A/index.md", "/tmp/docs/B/index.md"]
        self.assertEqual([self.extractor.normalize_file_path(p) for p in paths], paths)
        self.assertEqual(len({self.extractor.generate_document_id(p) for p in paths}), 2)
        self.assertEqual(self.extractor.normalize_file_path("test.md"), "test.md")

    def test_is_framework_main_page(self):
        """Test framework main page detection."""
        # Test index file
        self.assertTrue(self.extractor.is_framework_main_page("", "documentation/SwiftUI/index.md"))
        self.assertTrue(self.extractor.is_framework_main_page("", "documentation/UIKit/README.md"))
        
        # Test content-based detection
        content = "# SwiftUI Framework\n\nOverview of SwiftUI"
        self.assertTrue(self.extractor.is_framework_main_page(content, "test.md"))
        
        # Test non-main page
        self.assertFalse(self.extractor.is_framework_main_page("class View {}", "View.md"))
    
    def test_complete_metadata_extraction(self):
        """Test complete metadata extraction."""
        content = """# View

**Framework**: SwiftUI  
**Kind**: protocol

A type that represents part of your app's user interface.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
protocol View {
    associatedtype Body : View
    var body: Self.Body { get }
}
```

#### Overview

You create custom views by declaring types that conform to the View protocol.

```swift
struct MyView: View {
    var body: some View { Text("Hello, visionOS!") }
}
```

---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view)*
"""
        
        file_path = self.create_test_file(content, "documentation/SwiftUI/View.md")
        metadata = self.extractor.extract_metadata(content, file_path)
        
        # Verify all expected fields
        self.assertEqual(metadata["api_name"], "View")
        self.assertEqual(metadata["framework"], "SwiftUI")
        self.assertEqual(metadata["title"], "View")
        self.assertEqual(metadata["kind"], "protocol")
        # The Availability list, not the visionOS in the sample code
        self.assertEqual(metadata["platforms"], ["iOS", "macOS", "tvOS", "watchOS"])
        # Overview should come from the Overview section, not the first paragraph
        self.assertIn("You create custom views", metadata["overview"])
        self.assertFalse(metadata["is_framework_main"])
        self.assertEqual(metadata["url"], "https://developer.apple.com/documentation/swiftui/view")
        self.assertEqual(metadata["file_path"], "documentation/SwiftUI/View.md")

    def test_url_from_footer_verbatim(self) -> None:
        """The footer's URL, as scraped: not rebuilt from the sanitized file name."""
        content = ("# init(viewControllerProvider:)\n\n**Framework**: UIKit  \n**Kind**: init\n\n"
                   "---\n\n*[View on Apple Developer](https://developer.apple.com/documentation/uikit/"
                   "uisearchtab/init(viewcontrollerprovider:))*\n")
        file_path = self.create_test_file(content, "documentation/UIKit/uisearchtab/init-viewcontrollerprovider.md")
        metadata = self.extractor.extract_metadata(content, file_path)
        self.assertEqual(metadata["url"],
                         "https://developer.apple.com/documentation/uikit/uisearchtab/init(viewcontrollerprovider:)")

    def test_url_from_an_encoded_footer(self) -> None:
        """A URL Apple cut inside its argument list: its footer encodes the unclosed "("
        (markdown_url), and the page's URL, as scraped, is indexed; an older rendering
        has it as it is."""
        url = ("https://developer.apple.com/documentation/metal/mtlindirectrendercommand/"
               "drawindexedpatches(_:patchstart:patchcount-4mdz8")
        for written in (url.replace("patches(", "patches%28"), url):
            content = f"# drawIndexedPatches\n\n**Kind**: method\n\n---\n\n*[View on Apple Developer]({written})*\n"
            self.assertEqual(self.extractor.extract_source_url(content), url)
            path = self.create_test_file(content, "documentation/Metal/mtlindirectrendercommand/drawindexedpatches.md")
            self.assertEqual(self.extractor.extract_metadata(content, path)["url"], url)

    def test_url_without_footer(self) -> None:
        """Front matter's url first; a page with neither falls back to the path."""
        front = "---\nurl: https://github.com/swiftlang/swift-book/blob/main/A.md\n---\n\n# A\n"
        path = self.create_test_file(front, "documentation/Swift-Book/A.md")
        self.assertEqual(self.extractor.extract_metadata(front, path)["url"],
                         "https://github.com/swiftlang/swift-book/blob/main/A.md")
        bare = "# Index\n\nNo footer.\n"
        path = self.create_test_file(bare, "documentation/Swift-Book/Guide/index.md")
        self.assertEqual(self.extractor.extract_metadata(bare, path)["url"],
                         "https://developer.apple.com/documentation/swift-book/guide/index")
        # A footer that isn't the last line isn't the page's footer
        quoted = "# A\n\n*[View on Apple Developer](https://developer.apple.com/documentation/x/y)*\n\nMore.\n"
        self.assertIsNone(self.extractor.extract_source_url(quoted))

    def test_a_docc_site_page_under_its_namespace(self) -> None:
        """A DocC site's page (documentation/<namespace>/<Dir>/…, item 4): its front matter
        names its url and its framework label, and its footer names its site."""
        url = "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/buildparameters"
        content = ('---\nurl: "' + url + '"\nframework: "Swift-Org/PackagePlugin"\n---\n\n'
                   "# PackageManager.BuildParameters\n\n**Framework**: Swift-Org/PackagePlugin  \n"
                   "**Kind**: struct  \n**Role**: Structure\n\nParameters for a build.\n\n---\n\n"
                   f"*[View on docs.swift.org]({url})*\n")
        path = self.create_test_file(
            content, "documentation/Swift-Org/PackagePlugin/packagemanager/buildparameters.md")
        metadata = self.extractor.extract_metadata(content, path)
        self.assertEqual(metadata["framework"], "Swift-Org/PackagePlugin")
        self.assertEqual(metadata["url"], url)
        self.assertEqual(self.extractor.extract_source_url(content), url)
        self.assertEqual(metadata["api_name"], "BuildParameters")
        self.assertEqual(metadata["title"], "PackageManager.BuildParameters")
        self.assertEqual(metadata["kind"], "struct")
        self.assertEqual(metadata["overview"], "Parameters for a build.")

    def test_a_page_without_a_title_line_is_never_untitled(self) -> None:
        """A page without a "# " heading (MLX's mlx-lm README starts at "## MLX LM") takes its
        front matter's title, else its first heading of any level, else its file name; a
        "# " line in code is never its title."""
        front = "---\nsource: mlx-lm\nframework: MLX\nurl: https://github.com/ml-explore/mlx-lm/blob/main/README.md\n---\n\n"
        readme = front + "## MLX LM \n\nMLX LM is a Python package.\n\n```sh\n# install it\npip install mlx-lm\n```\n"
        path = self.create_test_file(readme, "documentation/MLX/mlx-lm/README.md")
        metadata = self.extractor.extract_metadata(readme, path)
        self.assertEqual(metadata["title"], "MLX LM")
        self.assertEqual(metadata["api_name"], "MLX LM")
        # A "# " heading after code is still the title; the "# " line in the code isn't
        code_first = "```python\n# not a title\n```\n\n## Setup ##\n\n# Real Title\n"
        self.assertEqual(self.extractor.extract_title(code_first), "Real Title")
        self.assertEqual(self.extractor.extract_title("~~~\n# no\n~~~\n\n### Third ###\n"), "Third")
        # The front matter's title before a lower heading
        self.assertEqual(self.extractor.extract_title("---\ntitle: Guide\n---\n\n## Part\n"), "Guide")
        # Nothing but text: the file name, when one is given
        plain = "Just text.\n\n```\n# code\n```\n"
        self.assertEqual(self.extractor.extract_title(plain, "documentation/X/getting-started.md"), "getting-started")
        self.assertEqual(self.extractor.extract_title(plain), "")
        self.assertEqual(self.extractor.extract_api_name(plain, "documentation/X/getting-started.md"),
                         "getting-started")

if __name__ == "__main__":
    unittest.main()