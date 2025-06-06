# Safari 17 Release Notes

**Framework**: Safari Release Notes

Released September 18, 2023 — Version 17 (19616.1.27)

#### Overview

Safari 17 is available for iOS 17, iPadOS 17, macOS Sonoma, macOS Ventura, and macOS Monterey.

##### Accessibility

###### New Features

- Added support for `code` ARIA role. (106621574)

###### Resolved Issues

- Fixed `aria-owns` attribute for the `radio` role. (23630121)
- Fixed incorrect accessible name from multiple `<label>` elements. (24033482)
- Fixed HTML menu element to map to `role=list`. (55145117)
- Fixed conveying focus movement when using `aria-activedescendant` to set the active cell within a grid. (84439987)
- Fixed the wrong role displayed for `input` in Web Inspector. (103907008)
- Fixed `input[type=date]` individual fields getting announced as “group”. (104928713)
- Fixed VoiceOver when selecting “Sign in with Apple” on some websites. (105179300)
- Fixed elements with the `popovertarget` attribute to expose expanded state to assistive technologies. (105425310)
- Fixed some inputs not being treated as invalid despite being rendered as such. (105653691)
- Fixed `aria-errormessage` to not be exposed when `aria-invalid` is `false`. (105813974)
- Fixed form controls taking the accessibility text of an ancestor label over their own inner text. (106575817)
- Fixed VoiceOver not reading entered text in text fields. (107226275)
- Fixed labels for slot elements referenced with `aria-labelledby`. (107570512)
- Fixed properly exposing lists that have `display: contents` list items. (107924637)
- Fixed `aria-activedescendant` to work for `display: contents` elements. (108248056)
- Fixed CSS `speak-as`, AXAccessKey, `aria-owns`, and URL AX APIs to work for `display: contents` elements. (108301432)
- Fixed `aria-grabbed` and `aria-dropeffect` to work for `display: contents` elements. (108349820)
- Fixed `aria-describedby` to be equivalent to `aria-description` and override it when both are present. (108386295)
- Fixed computing the wrong accessibility clickpoint for `display: contents` links and headings. (108409898)
- Fixed `display: contents` elements to be able to return selected accessibility children. (108428630)
- Fixed computing the accessible name for `display: contents` elements that rely on labels or captions. (108492642)
- Fixed `aria-flowto` to work for `display: contents` elements. (108542797)
- Fixed slotted elements not being exposed to accessibility when inside `<dialog>` or `aria-modal`. (108704582)
- Fixed `display: contents` lists to return the correct sub-role. (109498423)
- Fixed `aria-checked` to work for `role="treeitem"` elements with `display: contents`. (109955788)
- Fixed some content on web pages not displaying on braille displays. (110758833)
- Fixed table structure for elements with a `role` attribute of `grid`, `treegrid`, `table`, `row`, `gridcell`, `cell`, or `columnheader` with `display: contents`. (111193901)
- Fixed: Improved accessibility for tables and table components with `display: flex`, `grid`, `block`, `inline-block`, and `contents`. (111202843)
- Fixed: Prioritized HTML `required` attribute over `aria-required` when both are present. (111370591)
- Fixed unexpected speech synthesis behavior for unordered lists. (112085797)
- Fixed `display: contents` elements sometimes missing their children. (113044333)

##### Apple Pay

###### New Features

- Added support for Apple Pay in cross-origin iframes with the `allow="payment"` attribute. (88969594)

##### Authentication

###### New Features

- Added support for `largeBlob` extension for the local authenticator. (105237759)

##### Canvas

###### Resolved Issues

- Fixed `createImageBitmap` using `ImageData` to respect the premultiply flag. (89382358)
- Fixed repaint issue when drawing VideoFrames to canvas. (109100283)

##### Css

###### New Features

- Added support for `@counter-style`. (30318695)
- Added support for the `update` Media Query. (35799713)
- Added support for optional resolution and type arguments in `image-set()`. (77598590)
- Added support for `contain-intrinsic-size`. (89358231)
- Added support for `full-width` and `full-size-kana` values for `text-transform`. (100310853)
- Added support for multiple `text-transform` values. (105381249)
- Added support for `@supports font-tech()` and `@font-face { src: tech() }`. (105665900)
- Added support for the `@font-face` `size-adjust` descriptor. (106349717)
- Added support for `containerName` and `containerQuery` and updated `conditionText` to be “`containerName` `containerQuery`”. (106505281)
- Added support for `overflow-block` and `overflow-inline` media query features. (106511968)
- Added support for the two-value syntax of `font-size-adjust`. (107290850)
- Added support for `@supports font-format()`. (107381176)
- Added support for the `from-font` value for `font-size-adjust`. (107735982)
- Added `nowrap` white-space to the User-Agent Stylesheet for the `<option>` element. (110019702)
- Added support for the `scripting` media query. (110949545)
- Added support for `word-break: auto`. (111507205)
- Added support for `contain-intrinsic-size: auto none`. (111510558)
- Added support for `contain-intrinsic-size: inherit`. (112409855)

###### Resolved Issues

- Fixed CSS `@imports` in HTML missing quote marks getting mistakenly hidden from the Preload Scanner. (46031271)
- Fixed matching elements without a parent with the child-indexed pseudo-class. (91637426)
- Fixed the bug that `@supports selector()` fails for all `-webkit-` prefixed pseudo elements. (95683424)
- Fixed `background-size` to not accept unitless lengths. (97039770)
- Fixed `text-shadow` and `box-shadow` with `currentcolor`. (102542182)
- Fixed `color()` function incorrectly parsing missing components. (104679823)
- Fixed `text-emphasis` marks to not be rendered if there is no emphasized character. (104688963)
- Fixed: Improved `image-set` compatibility. (105097744)
- Fixed values set by `mask` and `background` shorthands to not serialize as “initial”. (105114588)
- Fixed `:has()` to support invalidation of `:buffering` and `:stalled` pseudo-classes. (105163364)
- Fixed `cssText` to follow CSS OM specifications. (105235157)
- Fixed `font-feature-settings` and `font-variation-settings` to sort their tags alphabetically. (105483635)
- Fixed `transition-property: all` to include custom properties. (105556538)
- Fixed `#x`, such as `1x`, to be recognized a resolution calc unit category. (105700660)
- Fixed font variations for some fonts declared with CSS `@font-face`. (106635029)
- Fixed applying certain user-agent styles to HTML elements, and not elements with other namespaces. (107162842)
- Fixed `image-set` to accept zero resolution and clamp negative resolutions used in calc expressions. (107167273)
- Fixed unknown function parsing in `@supports` rule. (107397723)
- Fixed to not show `cursor: pointer` on unclickable `<area>`. (107591470)
- Fixed `CSSStyleValue.parse` to accept properties from the document-derived context. (108249093)
- Fixed invalidating the `:dir()` pseudo-class after removing the `:dir` content attribute from the document element. (108480507)
- Fixed `type()` function for `image-set()` to only take one string. (108909363)
- Fixed respecting style containment on list items. (109582377)
- Fixed scrollbar to correctly pick up changed styles immediately. (109674102)
- Fixed `:has()` to support invalidation of the `:defined` pseudo-class. (109896689)
- Fixed `cjk-earthly-branch` and `cjk-heavenly-stem` counter styles to have `fixed` system. (110796633)
- Fixed `<ray-size>` to be optional in `ray()` for CSS Motion Path. (110818689)
- Fixed negative resolutions in Media Queries to be invalid. (110948170)
- Fixed `text-overflow: ellipsis` so it works with `overflow: clip`. (111182654)
- Fixed `cjk-earthly-branch` and `cjk-heavenly-stem` counter styles to fallback to `cjk-decimal`. (111208503)
- Fixed `inline-flex` and `inline-grid boxes` to stop propagating underlines to align with other browsers. (111228920)
- Fixed container units in a container query to evaluate against the ancestor container. (111446508)
- Fixed cursor style to respect explicitly set cursor type over system default. (111469521)
- Fixed container units to consider writing mode for unit resolution. (111565488)
- Fixed `@font-face { src: format() }`  to parse valid unsupported keywords. (112135869)
- Fixed `-webkit-box-decoration-break: clone` with left and right padding causes unexpected wrapping of inline content. (112197978)

##### Developer Tools

###### New Features

- Redesigned the Develop menu, including device and application icons for connected devices. (99830772)
- Added the ability to open the current page in a Simulator from Responsive Design Mode or the Develop menu. (99830918)
- Added Developer settings and Feature Flags to Safari settings. (100420018)
- Redesigned Responsive Design Mode. (100522676)
- Added support for pairing with tvOS and visionOS on macOS Sonoma. (103498148)

##### Dom

###### Resolved Issues

- Fixed XML serialization to serialize implicit `xmlns` attributes first and use lowercase “ns” when generating prefixes. (103234827)

##### Editing

###### New Features

- Improved interoperability for the Range API and Selection API. (100579464)
- Added a new appearance for marked text. (101869724)
- Added support for the caret color to match the accent color of the system on macOS. (102450017)

###### Resolved Issues

- Fixed webpage translation for iframes. (59693219)
- Fixed returning live range synchronized with selection from `getRangeAt` and throw errors as specified. (69015762)
- Fixed selection API to work across shadow boundaries. (89481826)
- Fixed webpage issues when translating to or from Ukranian. (100570016)
- Fixed showing the software keyboard when programatically focusing a text field during a double-click event. (104600783)
- Fixed “insertParagraph” to insert a `<br>` when the root editable element is phrasing content. (105438898)
- Fixed “insertLineBreak” sometimes inserting a non-breaking space instead of a new line. (105439065)
- Fixed an issue when breaking out of an empty list item in case of nested lists. (111724381)

##### Forms

###### New Features

- Added support for `<hr>` inside `<select>`. On macOS this is rendered as a separator. (107656886)

###### Resolved Issues

- Fixed CSS color getting adjusted for disabled input elements. (99826522)
- Fixed `input.validity` reporting `valid: true` for partially completed dates and times. (102984901)
- Fixed conditional passkey request presenting a conditional control even after `AbortController.abort()`. (104485543)
- Fixed `<input pattern>` to use the regular expression `v` flag rather than `u`. (105268069)
- Fixed saving recent searches on `<input type="search">` using the `name` attribute. (105369635)
- Fixed HTML `maxlength` attribute treating emoji of string length 11 as length 1. (105926915)
- Fixed `HTMLOptionsCollection.length` setter to use a limit of 100,000. (105988871)
- Fixed reseting selection when changing multiple `<select>` to single. (106264081)
- Fixed focus for a `<summary>` element with a `tabindex`. (106550778)
- Fixed selecting text within a label element that is linked to an input field. (108566491)
- Fixed textareas with `overflow: hidden` rendering too many columns. (109343502)
- Fixed HTMLOptionElement text setter to not throw an exception. (109740566)
- Fixed change event not firing when the user reverts the value of a color, date, or time input after JavaScript changed the value. (109843791)

##### Html

###### New Features

- Added experimental support for the `<model>` element. (100595523)
- Added support for the `popover` attribute. (104204093)
- Added support for the `<search>` element. (107175819)

###### Resolved Issues

- Fixed handling unclosed parenthese at the end of the `sizes` attribute. (107509739)
- Fixed the HTMLPreloadScanner to not preload scripts with unsupported types. (110905029)
- Fixed popover incorrectly auto-hiding when using shadow DOM. (112410375)

##### Http

###### New Features

- Added support for preconnect via HTTP early hints. (106055702)

###### Resolved Issues

- Fixed respecting Content-Type header for MIME type determination. (73343155)
- Fixed a bug with empty header values in Headers objects with “request-no-cors” guard. (105207779)
- Fixed Cross-Origin-Embedder-Policy incorrectly blocking an iframe on a cache hit. (107002434)
- Fixed `vary` header behavior for opaque responses. (107769146)

##### Images

###### New Features

- Added support for HEIC/HEIF images. (99517108)
- Added support for JPEG XL. (100641584)

##### Javascript

###### New Features

- Added support for RegExp duplicate named capture groups. (100335581)
- Added support for the RegExp `v` flag. (100337109)
- Added support for new `Set.prototype` methods. (105190165)
- Updated `Intl.Locale` to replace info getters with individual `get…` methods. (105570888)
- Added support for `Set.prototype.difference`. (106031487)

###### Resolved Issues

- Fixed: Improved performance of `Object.entries()` by 1.5×. (100783096)
- Fixed `/\p{Number}--]/v;` to be a syntax error. (109400589)
- Fixed: Improved RegExp lookbehind character class backtracking. (111051833)
- Fixed `String#charAt` to support out-of-bounds handling in DFG. (111421698)

##### Live Text

###### New Features

- Added support for vertical text recognition in images and videos. (101314828)

##### Lockdown Mode

###### New Features

- Disabled IndexedDB. (101187278)
- Disabled the File API and FileReader API. (101187306)
- Disabled support for the `<embed>` element. (101187413)
- Added support for select web fonts. (101523138)
- Added Lockdown Mode support to WebKit on watchOS. (101525499)
- Disabled support for experimental APIs. (101969455)
- Disabled the WebSpeech (SpeechSynthesis) API. (103316392)
- Disabled the WebLocks API. (103316423)

##### Media

###### New Features

- Added support for Managed Media Source on macOS and iPadOS, and added support as a preview on iOS. (30320350)
- Added support for AV1 codec support to the MediaCapabilities API for devices with hardware support. (97803066)
- Added support for enforcing low-power mode and optimize video streaming setting by tone mapping HDR video to SDR. (100597710)
- Added “Show Media Stats” when developer features are enabled in Safari. (108558776)
- Added support for making Managed Media Source available only when an AirPlay source alternative is present or remote playback is explicitly disabled. (109130836)
- Added support for WebCodecs temporal `scalabilityMode` for software codecs, including parsing and error handling. (110774875)
- Added support for stereo-only Opus in MPEG-4 and WebM containers on macOS Sonoma. (50994465)

###### Resolved Issues

- Fixed `top` CSS added to audio controls when the height of an `<audio>` element is adjusted on iOS. (99548840)
- Fixed Netflix.com playback error S7381-1203. (103561991)
- Fixed sound echos in higher speed video playback. (103940613)
- Fixed `SourceBuffer.timestampOffset` behavior with WebM content. (105801920)
- Fixed `bufferedchange` event to fire whenever an eviction occurs. (106168510)
- Fixed MediaSource duration change algorithm to correctly update the duration. (106858912)
- Fixed `playing` event to fire earlier. (107041118)
- Fixed video playback failure for content that uses the prefixed WebKit EME APIs. (107202864)
- Fixed Netflix.com playback error S7361-1253. (108052652)
- Fixed video playback in Safari unexpectedly interrupting other apps playing audio. (108741963)
- Fixed MediaRecorder producing empty chunks when attaching a MediaStream before the context in a canvas is created. (109705910)
- Fixed muting capture in all other tabs when Safari starts camera and/or microphone capture in a tab. (109896538)

##### Private Browsing

###### New Features

- Added blocking for known trackers and fingerprinting. (99360202)
- Added support for mitigating trackers that map subdomains to third-party IP addresses. (99360259)
- Added blocking for known tracking query parameters in links in Private Browsing. (99360362)
- Added noise to fingerprintable web APIs. (99360413)
- Added console log messages when blocking requests to known trackers. (100523322)
- Added support for blocking trackers that use third-party CNAME cloaking. (101612742)
- Added support for Private Click Measurement. (106245330)

##### Profiles

###### New Features

- Added support for enabling Safari Extensions per-profile. (99399845)
- Added support for Web Push subscriptions per profile. (100194363)

##### Rendering

###### Resolved Issues

- Fixed rendering for `border-image-repeat: round`. (28213711)
- Fixed `text-overflow: ellipsis` incorrectly truncating text in right-to-left mode. (29464657)
- Fixed rendering fractional font sizes. (40829933)
- Fixed rendering the `label` attribute for the `<option>` element on iOS. (53989128)
- Fixed pixel artifacts when rendering `background-clip: text` and `transform: rotate(…)`. (54325642)
- Fixed text not getting truncated properly in vertical writing mode when `overflow: hidden` and `text-overflow: ellipsis` are set. (94330690)
- Fixed CSS flexbox to use initial scroll position when computing the baseline. (100908615)
- Fixed incorrect paint of `translate` property animation. (102064448)
- Fixed statically positioned out-of-flow box location when display type changes from `block` to `inline-block`. (103637239)
- Fixed `<details>` marker maintain the same margin in right-to-left as in left-to-right. (104275835)
- Fixed table with fixed layout behaving like auto layout when its width is set by JavaScript instead of CSS. (105310280)
- Fixed `preserve-3d` to apply to pseudo-element children. (105474987)
- Fixed margins incorrectly accounting for before forced breaks in multi-column layout. (105631038)
- Fixed placement of floats with `clear`. (105775276)
- Fixed disabling `<body>` to root propagation when `content: paint` is set on the `<body>` or the root. (105850374)
- Fixed self-collapsing children with an incorrect top offset at the end of a block container with `margin-trim: block-end`. (106524654)
- Fixed ignoring `calc()` values on `<colgroup>` elements. (106692191)
- Fixed a flash of mis-styled content due to a mechanism to block painting on a non-final style. (106805458)
- Fixed text wrapping in a nested grid layout. (107002717)
- Fixed width for a table `flex-item` inside `inline-flex` with column `flex-direction`. (107029563)
- Fixed repaint issue when adding text to a text box. (107038111)
- Fixed incorrect out-of-flow box placement for `display: inline` content when `text-align` is not `start`. (107271178)
- Fixed incorrect out-of-flow box placement for `display: inline` content when `text-indent` is present. (107280354)
- Fixed incorrect out-of-flow box placement for `display: inline` content when a float is present. (107294351)
- Fixed repainting newly position float boxes. (107318350)
- Fixed out-of-flow inline content with a float and `text-align`. (107321638)
- Fixed gradient object generation to be thread-safe. (107574124)
- Fixed `transform-style: preserve-3d` preventing links when `:after` has a negative `z-index`. (107671388)
- Fixed repainting MathML element in `display: flex` on content change. (107694159)
- Fixed `line-height` to not affect the enclosing height. (107832246)
- Fixed incorrect decorating box position in vertical writing mode. (107916341)
- Fixed incorrect vertical positioning when an ideographic baseline is present. (107934783)
- Fixed missing underline after the first character in `contenteditable`. (107996603)
- Fixed rendering a checkbox in a flexbox layout. (108026194)
- Fixed `-webkit-line-clamp` overlapping blocks even with `overflow: hidden`, when mixing `<span>` and `<div>`. (108116069)
- Fixed content getting truncated too early due to subpixel flooring. (108570251)
- Fixed negative `letter-spacing` breaking `-webkit-box-decoration-break: clone`. (108701795)
- Fixed images with `decoding="async"` flickering while zooming in. (108930635)
- Fixed overlapping list items when content has `line-height: 0`. (108988226)
- Fixed `alt` text rendering horizontally in vertical writing mode. (109004347)
- Fixed mapping `align="abscenter"` to `vertical-align: middle` (109081191)
- Fixed complex text paths to not render visible tab glyphs. (109171681)
- Fixed `overflow: clip` when an intrusive float is present. (109293228)
- Fixed fragmentation of content with non-visible overflow when printing. (109320964)
- Fixed incorrectly including the scrollbar thickness in the logical height of a textarea with `overflow: auto`. (109384976)
- Fixed `bordercolor` attribute on table elements to not create a visible border. (109436009)
- Fixed inline-level elements with a self-painting layer rendering overlapping ellipsis. (110408920)
- Fixed list alignment when a list item has a flex container. (111217986)
- Fixed canvas not showing the results of `CanvasRenderingContext2D.putImageData` until a forced re-render. (112901862)

##### Safari Extensions

###### New Features

- Added support for turning on or off extensions and content blockers in Private Browsing mode. (17933284)
- Added support for per-site permissions for Safari App Extensions. (84104594)
- Added support for syncing the state of Safari App Extensions across multiple macOS devices. (86430510)
- Added support for showing Content Blockers, the “On Other Devices” section, and a link to the App Store in the Manage Extensions view. (98330674)
- Added support for `regexSubstitution` in `declarativeNetRequest`. (100039848)

###### Resolved Issues

- Fixed the script API not returning a result when the `func` parameter is used. (100034937)
- Fixed WebNavigation events to no longer fire for webpages where the extension hasn’t been granted access. (100191647)
- Fixed `scripting.executeScript` return types. (107044691)

##### Storage

###### New Features

- Added complete support for the Storage API. (84280909)
- Added support for overwriting the `move` method for FileSystemHandle. (105858983)
- Added support for `StorageManager.estimate()`. (106169267)
- Added support for calculating quota based on disk space. (107711361)

###### Resolved Issues

- Fixed removing HTTP credentials when the data store is removed. (106728064)

##### Svg

###### Resolved Issues

- Fixed SVG `textLength` behavior. (32066826)
- Fixed references for SVG fragments in shadow DOM trees. (64094920)
- Fixed `overflow="visible"` having no effect on the dimension of a `<use>` element unless its dimensions are specified. (98577733)
- Fixed mixed characters in right-to-left mode for SVG text. (101695671)
- Fixed marker properties to allow any URI. (105483685)
- Fixed text transformation not starting on initial render. (106485848)
- Fixed `<marker orient="-1">` to orient correctly. (109312083)
- Fixed `animateMotion` to accumulate properly with `rotate: auto` or `rotate: auto-reverse`. (109489241)
- Fixed nested use of the same SVG resource. (109917889)
- Fixed computed `display` property for SVG elements. (109928375)
- Fixed to not create an interval if a value in `begin-value-list` doesn’t have a matching value in `end-value-list`. (109935392)
- Fixed `textLength` whitespace and chunk handling for `<tspan>` elements. (109981392)
- Fixed the mapping from a point to a character index for the SVG `<text>` element. (110119702)
- Fixed handling of a negative radius for `feMorphology`. (110504653)

##### Tables

###### Resolved Issues

- Fixed `table-layout: fixed` not getting applied when the width is `max-content`. (105627723)
- Fixed computing the percentage height of table cell children by removing the height of a horizontal scrollbar. (105627946)
- Fixed percentage sizing of table cell replaced children with a scrollbar. (108459503)

##### Web Animations

###### Resolved Issues

- Fixed logic to recompute keyframe styles to tie a change in computed keyframes on an accelerated animation while animating. (87766485)
- Fixed handling `transition-property: all` to distinguish matching any CSS property or Animation object. (87785199)
- Fixed keyframes to be recomputed when `bolder` or `lighter` is used on a `font-weight` property. (105098349)
- Fixed the composite operation of implicit keyframes for CSS Animations to be “replace”. (105099774)
- Fixed keyframes to be recomputed when a parent element changes value for a custom property set to `inherit`. (105099874)
- Fixed the `all` value for the `transition-property` to parse as a keyword, not a CSS property. (105556116)
- Fixed exposing `CSSKeyFramesRule.length`. (105565920)

##### Web Api

###### New Features

- Added support for 3D OffscreenCanvas WebGL support. (39882956)
- Added `canvas.drawImage` support for SVGImageElement as an image source. (79555760)
- Added support for `<link rel="modulepreload">`. (88670991)
- Added support for the [`focus fixup rule`](https://developer.apple.comhttps://html.spec.whatwg.org/multipage/interaction.html#focus-fixup-rule). (89902824)
- Added support for using relative URLs in the WebSocket constructor and HTTP(S) schemes. (101929623)
- Added support for Ed25519 cryptography. (105264767)
- Added support for `URL.canParse()`. (106934916)
- Added support for `customElements.getName` method. (108411398)
- Added support for two-parameter `delete()` and `has()` on URLSearchParams. (108949109)
- Added experimental support for priority to CSS Highlight API. (110125853)

###### Resolved Issues

- Fixed Canvas context allocation failures due to exceeding the maximum canvas memory limit. (48609162)
- Fixed firing an unexpected `mousemove` event when a modifier key is pressed. (81287778)
- Fixed HTML comments added after `<body>` to not be included in `document.body.innerHTML`. (95557786)
- Fixed serialization of Selectors. (97092572)
- Fixed string serialization of functions to match other browsers. (97445158)
- Fixed `screen.colorDepth` reporting the incorrect value on iOS. (99871925)
- Fixed valid values for the `as` property in `<link rel="preload">`. (100161255)
- Fixed: Improved GamePad compatibility with XBOX Cloud. (100337662)
- Fixed: Improved Fetch API interoperability. (100582566)
- Fixed the Content-Type for sliced blobs in `fetch()`. (101171705)
- Fixed Blob range requests. (103171187)
- Fixed: Adjusted text input `scrollWidth` and `scrollHeight` to include padding and any whitespace added by decorations. (104332108)
- Fixed `focus()` method with `delegatesFocus` in Shadow DOM. (104927020)
- Fixed Range APIs to construct and move trees in tree order. (105154132)
- Fixed handling magnitude values passed to `GamepadHapticActuator.playEffect()`. (105175808)
- Fixed `Gamepad.vibrationActuator.type` to be `dual-rumble`. (105175859)
- Fixed `location.href` to throw a SyntaxError on a URL parser failure. (105631453)
- Fixed the natural screen orientation on iPad and TV to be landscape-primary. (106062507)
- Fixed `postMessage` for cross-origin iframes. (106439413)
- Fixed `Worklet.prototype.constructor`. (106533500)
- Fixed `innertHTML` serialization to not have special handling for `javascript:` URLs. (107362610)
- Fixed not escaping `<`, `>`, `&`, and non-breaking space characters inside  `<noembed>`, `<noframes>`, and `<plaintext>` elements when scripting is enabled. (107381507)
- Fixed CacheStorageManager creating a “salt” file in the current working directory when there is no path. (107387306)
- Fixed to no longer recognize the SVG `contentScriptType`, `contentStyleType`, and `externalResourcesRequired` attributes, and the XML `xml:base` attribute. (107428878)
- Fixed Non-UTF-8 encoders to correctly emit the U+FFFD code point instead of surrogate code points. (107530253)
- Fixed `document.applets` to no longer return any elements. (107926196)
- Fixed `data:` URLs to behave the same everywhere. (107982669)
- Fixed missing `movementX` and `movementY` in `pointermove` events. (108112600)
- Fixed Wake Lock permission denied after `visibilitychange`. (108279602)
- Fixed `<frameset>` inside `<template>` to be ignored. (109081113)
- Fixed node depth computation for shadow nodes in ResizeObserver. (109166329)
- Fixed WebSocket’s `binaryType` setter to not throw. (109192086)
- Fixed exposing `DeviceMotionEvent` and `DeviceOrientationEvent` on the global `Window` object on macOS. (109580299)
- Fixed remaining page height to never be 0. (109929893)
- Fixed changing the `dir` attribute of `documentElement` not updating a child element matching the `:dir` pseudo-class. (109976294)
- Fixed: Set canvas-based VideoFrame color space to RGB. (110062111)
- Fixed `window.stop()` to fire abort events on XMLHttpRequest asynchronously. (110086856)
- Fixed selecting an OptGroup label not unselecting the selected item. (110088331)
- Fixed `<select>` with multiple enabled not consistently firing the `onchange` event. (110274850)
- Fixed style invalidation of IDs within `:nth-child` and `:nth-last-child`. (110451692)
- Fixed MediaStream from a canvas (captureStream) to be able to render into a different canvas. (110696945)
- Fixed `XMLHttpRequest.responseXML.characterSet`. (110863647)
- Fixed window named getter to behave correctly when there are duplicate frame names. (110864556)
- Fixed: Throttled `mousemove` events to one per rendering. (110921187)
- Fixed Service Worker redirect losing the hash fragment. (111208014)
- Fixed camera RAW files picked via file input getting returned as PNG on change. (111231838)
- Fixed emoji characters sometimes getting incorrectly drawn in text style. (111411175)
- Fixed `HTMLTableSectionElement.insertRow(0)` and `HTMLTableRowElement.insertCell(0)`. (111791597)

###### Deprecations

- Stopped parsing `<command>` as if it has no end tag. (107416609)
- Removed vestigal support for `<layer>` and `<nolayer>` from the HTML parser. (107554605)
- Removed deprecated uppercase URL attribute alias on the WebSocket interface. (109151597)

##### Web Apps

###### New Features

- Added support for web apps on macOS Sonoma. Add any website to the Dock from the File menu or Share Sheet to get to them even faster. Web apps open in their own window, and integrate with system features like Stage Manager, Screen Time, Notifications, and Focus. (68606770)
- Added support for Notification alert sounds. (107424158)

###### Resolved Issues

- Fixed passing `NotificationOptions.silent`. (107424158)
- Fixed: Started using origin directory for DOMCache and ServiceWorkerRegistrations. (107843591)
- Fixed Notifications API to default silent to the platform convention. (109390045)
- Fixed Web Push notifications not working in some cases by running the service worker before firing the `activate` event. (109411104)
- Fixed service worker downloads failing when chunks are sent via `postMessage`. (109561888)
- Fixed firing `controllerchange` event when a service worker gets deleted. (109567316)

##### Web Inspector

###### New Features

- Added pretty-printing support for various modern JavaScript syntax, including optional chaining, private class members, and optional assignment operators. (89097522)
- Added support for showing grid and flex overlays when in element selection mode. (105041619)
- Added the Color Scheme toggle to user preferences overrides popover. (105186265)
- Added support for showing rulers when highlighting elements in element selection mode. (105504143)
- Added editing controls for variation axes in the Fonts sidebar of the Elements tab. (106110217)
- Added support for ES2022 Private Fields when inspecting and logging JavaScript objects. (107863310)
- Added support for viewing the target of a `WeakRef`. (109475228)

###### Resolved Issues

- Fixed removing a CSS declaration when tabbing though the CSS selector in the Styles panel. (100492875)
- Fixed Step Over behaving like Resume when stepping over a function with a falsy conditional breakpoint in the Sources tab. (101604843)
- Fixed the box model to indicate a margin has been trimmed with `margin-trim`. (103374677)
- Fixed “Inspect Element” not highlighting the selected element. (105177739)
- Fixed display of `color-mix` CSS in the Styles sidebar of the Elements tab. (105732322)
- Fixed failing to add a new CSS rule on the first attempt in the Elements tab. (106751396)
- Fixed Web Inspector to not show the accessibility role in hover tooltips for elements where accessibility is ignored. (106771408)
- Fixed missing console logging that occurs during main frame navigation in the Console tab. (106877298)
- Fixed cleared items in the Network tab reappearing when Preserve Log is enabled. (107639797)
- Fixed incorrect timestamps in the Console tab. (107660054)
- Fixed non-enumerable properties appearing as though they are internal properties in the Console tab. (108005425)
- Fixed internal properties not greyed-out in object previews in the Console tab. (108007438)
- Fixed private symbols to be omitted in the scope chain. (108674026)
- Fixed an issue where the width of the Sources details sidebar would reset when switching between Web Inspector tabs (109253229)
- Fixed the error message for `new URL("/")` to be more explicit. (109253920)
- Fixed editing for Local Storage that appears truncated. (109473191)
- Fixed the resource type shown in the Network tab to use XHR when the XHR request has the same URL as the main resource. (110016863)
- Fixed color swatch to not show an incorrect tooltip when read-only. (110409252)

##### Webgl

###### New Features

- Added support for `EXT_disjoint_timer_query` (30054979)
- Added support for `WEBGL_clip_cull_distance` (105178437)
- Added support for `EXT_disjoint_timer_query_webgl2` (105630255)
- Added support for `EXT_polygon_offset_clamp` (105987827)
- Added support for GPUExternalTexture. (108463707)

###### Resolved Issues

- Fixed firing the context lost event for OffscreenCanvas. (104198422)
- Fixed OffscreenCanvas to work as a TexImageSource in WebGL. (106700463)

##### Webrtc

###### New Features

- Added support for inbound rtp `trackIdentifier` stat field. (105197543)
- Added support for exposing `zoom` in MediaTrackCapabilities. (106498125)
- Added support for `InputDeviceInfo`. (106716244)
- Added support for `getDisplayMedia` video track clone resizing. (106755005)

###### Resolved Issues

- Fixed preventing the display from going to sleep when the camera is on. (100423979)
- Fixed layer context handling for the HTMLMediaElement. (105795272)
- Fixed ending a muted microphone track when its device disappears. (108194510)
- Fixed camera selection to use the system preferred camera on iOS. (109220107)
- Fixed camera and microphone to all have `groupIds`. (109355290)

##### Wkwebview

###### New Features

- Added support for trying HTTPS for all navigations. (100477884)
- Added support for the Proxy API. (100583135)
- Added support for inline predictions for autocomplete. (105197136)

## See Also

- [Safari 17.6 Release Notes](safari-17_6-release-notes.md)
  Released July 29, 2024 — 17.6 (19618.3.11)
- [Safari 17.5 Release Notes](safari-17_5-release-notes.md)
  Released May 13, 2024 — 17.5 (19618.2.12)
- [Safari 17.4 Release Notes](safari-17_4-release-notes.md)
  Released March 5, 2024 — 17.4  (19618.1.15)
- [Safari 17.3 Release Notes](safari-17_3-release-notes.md)
  Released January 22, 2024 — Version 17.3 (19617.2.4)
- [Safari 17.2 Release Notes](safari-17_2-release-notes.md)
  Released December 11, 2023 — Version 17.2 (19617.1.17)
- [Safari 17.1 Release Notes](safari-17_1-release-notes.md)
  Released October 25, 2023 — Version 17.1 (19616.2.9)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-17-release-notes)*