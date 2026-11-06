# Safari 27.3 Beta Release Notes

**Framework**: Safari Release Notes  
**Role**: Article

Released November 3, 2026 — 27.3 beta (20626.1.12)

## Overview

Safari 27.3 beta is available for iOS 27.3 beta, iPadOS 27.3 beta, visionOS 27.3 beta, macOS 27.3 beta, macOS 26, and macOS Sequoia.

### Accessibility

#### Resolved Issues

- Fixed the accessible name of a `display: contents` element incorrectly including text from its siblings. (185108892)
- Fixed list marker text being included in accessible names and values that requested text without list markers. (185422271)
- Fixed list, table, tree, and canvas content being omitted from the accessible name or description when the containing element is referenced by `aria-labelledby` or `aria-describedby`. (186015032)
- Fixed an issue where VoiceOver announced `aria-keyshortcuts` values containing `Meta` or `Alt` literally instead of using the macOS terminology `Command` and `Option`. (186342070)
- Fixed the list marker missing from the accessibility text of a list item with block content. (186687365)
- Fixed VoiceOver on iOS automatically expanding `<select>` and date pickers after swiping from a text field. (187789276)
- Fixed VoiceOver announcing every focused ARIA menu item as “selected”. (188921930)
- Fixed VoiceOver being unable to press buttons with `pointer-events: none`. (188980125)
- Fixed VoiceOver activation dispatching `click` events with a `detail` of `0` and no pointer events, so they now mimic a mouse click. (189417259)
- Fixed text hidden with `clip` and `overflow: hidden` still being exposed in the accessibility tree. (189824370)
- Fixed VoiceOver being unable to reach the content of an `<iframe>` nested inside an iframe with `role="none"` or `role="presentation"`. (190043178)
- Fixed the `content` of a `::marker` pseudo-element not being exposed in the accessibility tree. (190150062)
- Fixed VoiceOver on iOS dispatching two sets of `pointerdown` events on pages with touch or pointer event listeners. (191127608)

### Animations

#### New Features

- Added support for running accelerated time-based animations in the remote layer tree to match how accelerated Scroll-driven Animations are run since Safari 26.3. Accelerated animations are animations targeting `transform` and individual transform CSS properties, `opacity`, `filter` and `backdrop-filter`. Animations that target the `offset` property, composed animations, animations that have a `playbackRate` other than 1 and animations that use the `linear()` and `steps()` easing functions are now also accelerated. (190761783)

#### Resolved Issues

- Fixed an issue where calling `play()` on a finite scroll-driven animation timeline did not reset its start time to the current time. (181712713)
- Fixed an issue where `animation-timeline` did not use the last matching timeline when it matched multiple timelines. (182405676)
- Fixed an issue where `animation-timeline` could match a timeline outside the nearest `timeline-scope` element with that name. (182417407)
- Fixed an unresolved current time for a progress-based timeline being treated as a progress timeline boundary. (183902668)
- Fixed an animation of `width` or `height` being incorrectly accelerated when only some keyframes have a size-dependent `transform`. (185153675)
- Fixed view timeline range boundaries discarding subpixel adjustments for sticky positioned elements. (185162728)
- Fixed keyframes using `revert-layer` or `revert-rule` no longer being recomputed after a `KeyframeEffect` is copied. (185164643)
- Fixed scroll-driven animations with a zero-length attachment range, such as `contain 50% contain 50%`, producing infinite computed keyframe offsets. (185204758)
- Fixed `scroll-timeline-name` and `view-timeline-name` to be loosely matched across shadow tree boundaries. (185206745)
- Fixed `getAnimations()` returning animations on `::picker-icon` and `::-webkit-scrollbar` pseudo-elements in the wrong composite order. (185270753)
- Fixed an issue where an animation attached to a view timeline’s scroll range was not updated when the scroll container’s scrollable overflow changed. (185328465)
- Fixed style-originated scroll timelines to match globally, allowing them to be defined outside of the target’s hierarchy or that of an element with a `timeline-scope` property. (186261285)
- Fixed an issue where a style-originated timeline defined outside of a `timeline-scope` hierarchy could remain active instead of yielding an inactive timeline. (186330965)
- Fixed an issue where changing a `timeline-scope` value did not update timelines for animations outside of its hierarchy. (186331685)
- Fixed an issue where the `ViewTimeline` constructor did not require a `subject` parameter. (187200265)
- Fixed the text cursor being misaligned in an input while an animation is running, by reverting a change to accelerated animation style invalidation. (190732406)

### Browser

#### New Features

- Vertical Tabs introduces a new vertical layout for navigating and managing tabs with a space-efficient design that maximizes webpage content.  (188851209)

### CSS

#### New Features

- Added support for `hyphenate-limit-chars` to set the minimum word length and the minimum number of characters before and after a hyphenation break. (23309642)
- Added support for `@supports at-rule(...)` conditions. (87884897)
- Added support for the `path()` and `shape()` functions in `shape-outside`. (93178320)
- Added support for a custom `<string>` value in `text-overflow`, so overflowing inline content can be truncated with any string instead of only `clip` or `ellipsis`. (94415937)
- Added support for the extended numeric range in longhand East Asian counter styles. (109875198)
- Added support for the `object-view-box` property. (132624217)
- Added support for the `attr()` function. (173992627)
- Added support for `property-scoped` and `property-index-scoped` caching keywords in `random()`. (176395332)
- Added support for `outline-offset: inset`. (180547604)
- Added support for the `@function` custom functions rule. (181625123)
- Added support for the `if()` function. (181806268)
- Added support for the `random-item()` function. (181816677)
- Added support for `calc-mix()`. (181839626)
- Added support for `justify-self` on block-level boxes. (181926245)
- Added support for a comma-separated list of conditions in `@container` queries. (182249814)
- Added support for `CSSContainerRule.conditions`. (182257864)
- Added support for the `content` property on the `::marker` pseudo-element. (182750380)
- Added support for the `text-decoration-inset` property. (182750933)
- Added support for the `white-space-trim` property. (182751076)
- Added support for the `wrap-inside` property. (182751559)
- Added support for `@supports named-feature()` conditions. (183688843)
- Added support for `HighlightRegistry.highlightsFromPoint()`. (184150480)
- Added support for `random()` in custom properties. (184715508)
- Added support for the `ident()` function. (184732904)
- Added support for the `inherit()` function. (184738624)
- Added support for `CSSConditionRule.supports`. (184943650)
- Added support for the `corner-shape` property. (184950973)
- Added support for the unprefixed `user-select` CSS property. (184964807)
- Added support for `CSSMediaRule.matches`. (185154835)
- Added support for using `sibling-index()` and `sibling-count()` within container query conditions. (186564084)
- Added support for `::highlight` to style all custom highlights at once. (186700364)
- Added support for the unprefixed `hyphenate-limit-lines` property, including interpolation, while keeping `-webkit-hyphenate-limit-lines` as an alias. (187173699)

#### Resolved Issues

- Fixed a background image not being repainted when only the URL fragment identifier changes. (105118256)
- Fixed an issue where a near-zero fixed `background-size` value collapsed the image tile to nothing. (140387662)
- Fixed outside list markers disappearing or being mispositioned around line breaks. (159277763)
- Fixed an issue where the `[class~=foo]` attribute selector did not perform as well as an equivalent class selector. (164128575)
- Fixed an issue where setting `view-transition-name` dynamically did not create a stacking context. (178316558)
- Fixed the computed value of `outline-offset` not being snapped as a line width. (180054053)
- Fixed an issue where CSS Grid items with a computed preferred size that behaves as `auto` did not correctly compute their minimum content contribution. (181146154)
- Fixed an issue where visually overflowing content in a CSS Grid item may not have been painted. (181277780)
- Fixed an issue where an empty editable flex container did not reserve a line’s worth of block size in vertical writing modes. (181485387)
- Fixed `:focus-visible` being shown after calling `focus()` inside an already focused ancestor. (181570771)
- Fixed an issue where CSS Grid did not correctly increase track sizes to accommodate items spanning flexible tracks. (181635324)
- Fixed an issue where stretch alignment did not trigger stretch sizing for CSS Grid items. (181750071)
- Fixed an issue where CSS Grid items could retain stale block sizes after a subsequent layout. (182144347)
- Fixed multi-column height ignoring `min-height` when it exceeds `max-height`. (182381903)
- Fixed an issue where `clip-path` shapes could render with incorrect arcs. (182443333)
- Fixed an issue where `::highlight()` and `::target-text` ignored `text-underline-offset`. (182466757)
- Fixed an issue where `::highlight()` decoration replaced the originating element’s decoration instead of layering over it. (182523249)
- Fixed `random()` and `random-item()` with an `auto` caching key in the same property value producing the same random value. (182846761)
- Fixed the serialization of an unrecognized media query to preserve the original text as closely as possible. (182958311)
- Fixed the serialization of an unrecognized media query feature name to preserve the original casing. (183065105)
- Fixed the originating element of `::part()` in `@container` queries to be the element itself. (183154183)
- Fixed `::highlight()` pseudo-elements not inheriting from the parent element’s highlight. (183702060)
- Fixed trailing whitespace not being trimmed when setting a style property to a value containing `var()`, `env()`, or `attr()` through the CSSOM. (183735232)
- Fixed `clip` on a child being ignored when determining whether an ancestor’s background is obscured. (183841775)
- Fixed `var()` not behaving as an arbitrary substitution function. (183913427)
- Fixed margins trimmed by `margin-trim` being reflected in computed style per CSSWG resolution. (184215336)
- Fixed the computed value of `line-height` to more closely match how it was specified. (184232888)
- Fixed `font-*` properties resolving font-relative units against their own font instead of the parent element’s font metrics. (184336424)
- Fixed the `rangeStart` and `rangeEnd` animation attributes accepting length values that are not computationally independent when set from script. (184363719)
- Fixed `-webkit-text-stroke` not applying to highlighted text. (184375039)
- Fixed the `ViewTimelineOptions` `inset` member accepting length values that are not computationally independent when set from script. (184504829)
- Fixed subgrid columns ignoring the parent grid’s content distribution from `justify-content`. (184542148)
- Fixed `::highlight()` not repainting after a CSS rule change. (184643272)
- Fixed `::highlight()` not repainting when a highlight’s range is changed with `CSS.highlights.set()`. (184672580)
- Fixed a `@function` body not inheriting computed custom property values from the calling context. (184701762)
- Fixed arguments that invoke a `@function` being treated as a cycle. (184711017)
- Fixed the `random()` caching key not including the custom property name. (184722866)
- Fixed the resolution of font-relative lengths when a minimum font size is in effect. (184727481)
- Fixed an issue where grid item margins were not included in the intrinsic size contributions of a grid container. (184789473)
- Fixed an `auto` `<random-key>` not being element-scoped, so every element shared the same item. (184845561)
- Fixed an issue where extra space was not distributed beyond growth limits when sizing grid tracks. (184933769)
- Fixed `::selection` failing to repaint when its style changes. (184994906)
- Fixed `getComputedStyle()` returning stale values for elements in the shadow tree of a `display: none` host after an inherited property changed on the host. (185079066)
- Fixed invalidation and serialization of properties that use `attr()` with a number or percentage value. (185088893)
- Fixed `anchor(right)` not resolving to an inline anchor’s right edge in `vertical-rl` writing mode. (185108663)
- Fixed `px` values inside `calc()` expressions being serialized incorrectly in computed style when `zoom` is applied. (185156231)
- Fixed font load status changes being reported with an incorrect previous state when script runs in response to a `FontFace` `loaded` promise. (185462848)
- Fixed incorrect style sharing between elements when a computed value depends on the `lh` unit. (185508307)
- Fixed: Removed the `inline`, `inline-start`, and `inline-end` values from `margin-trim`, which now accepts `none | block | [ block-start || block-end ]`. (185527437)
- Fixed an issue where outside list markers were only repositioned after layout when their first formatted line was in a descendant block, instead of for every outside list marker. (185529863)
- Fixed: Changed `calc()` simplification so that `clamp(none, a, b)` becomes `max(a, b)` and `clamp(a, b, none)` becomes `min(a, b)`. (185531467)
- Fixed `align-content` moving a floated child twice in block containers. (185536955)
- Fixed an issue where an inset `box-shadow` with a large spread on a wrapped inline element painted outside the element as full-width bands. (185651318)
- Fixed an issue where `CSS.highlights` iterated in hash order instead of registration order after its wrapper was garbage collected. (185754041)
- Fixed `background-size: contain`, `background-size: cover`, and automatic sizing ignoring SVG images that have one intrinsic dimension and no aspect ratio. (185970333)
- Fixed `:target` no longer matching an element after it was removed from the document and inserted again. (186059506)
- Fixed an issue where a grid item with an `aspect-ratio` could keep a stale inline size contribution when the grid container shrank. (186101273)
- Fixed an issue where flexible grid tracks did not respect the grid container’s minimum and maximum size. (186103325)
- Fixed an issue where fixed grid track sizing functions were overridden to zero while sizing tracks to fit non-spanning items. (186117142)
- Fixed an issue where explicitly-placed grid items advanced the auto-placement cursor. (186118858)
- Fixed an issue where the propagated root background was painted in the wrong position in `vertical-rl` writing mode. (186274088)
- Fixed `shape-outside` placing the shape in the wrong position when the float has margins. (186327525)
- Fixed an issue where a typed parameter of a CSS custom function did not keep its type. (186439114)
- Fixed an issue where `attr()` stopped invalidating on attribute changes after a view transition. (186467515)
- Fixed an issue where `fit-tolerance` did not interpolate between `<length-percentage>` values. (186509338)
- Fixed an issue where a grid item’s automatic minimum size was not clamped to a fixed maximum track sizing function. (186606479)
- Fixed a regression where the line-height quirk in quirks mode was not applied to line boxes inside a nested `inline-block` element that had no `line-height` of its own. (186614663)
- Fixed an issue where interpolating a `<length-percentage>` from a `calc()` value to a pure `<length>` dropped the percentage component at 100% progress. (186628152)
- Fixed an issue where `text-decoration-thickness` and `text-underline-offset` did not preserve percentage values when interpolating. (186628810)
- Fixed an issue where `text-indent` moved an outside list marker along with the indented text. (186678552)
- Fixed an issue where a float in a list item’s content pushed the outside list marker inward with the line. (186680551)
- Fixed an issue where a tab character rendered too narrow when `tab-size` was small in a proportional font. (186698040)
- Fixed an issue where a gradient in the `content` property painted blank. (186742805)
- Fixed an issue where `fit-content()` grid tracks could be stretched beyond their argument instead of capping the track’s growth limit. (186961437)
- Fixed an issue where an orthogonal `<caption>`’s margins were missing from the table. (187137359)
- Fixed an issue where an orthogonal `<caption>` ignored its margin against the table edge. (187139068)
- Fixed an issue where transforming a table row group could misplace its absolutely positioned children. (187252945)
- Fixed an issue where the resolved `right` and `bottom` values of an out-of-flow positioned element were wrong inside a vertical inline containing block. (187295559)
- Fixed an issue where the identity and translation fast path of a transformation matrix ignored the `w` component when mapping a 4-component point. (187297446)
- Fixed `@container` style queries on a pseudo-element’s host element using outdated style data. (187814567)
- Fixed layout performance for percentage `flex-basis` in nested column flex containers. (188404460)
- Fixed elements with `aspect-ratio` not shrinking inside a column `display: flex` container. (188649852)
- Fixed `aspect-ratio` being ignored on out-of-flow boxes with `height: fit-content`, `min-content`, or `max-content`. (188834114)
- Fixed table cells after a `width: 0` column being positioned incorrectly. (188939862)
- Fixed the initial value of `position-visibility` to be `anchor-visible`. (189049110)
- Fixed grid items with `aspect-ratio` and a percentage height not shrinking when the grid became narrower. (189253538)
- Fixed scroll snap animation taking a long time to settle on iOS after flicking past the last snap position. (189473962)
- Fixed word joiners breaking punctuation wrapping. (189968795)
- Fixed `light-dark()` inside `image-set()` incorrectly accepting a bare string as an image URL. (190560743)
- Fixed `document.fonts.ready` never resolving when an unused `@font-face` has a failing `local()` source followed by a `url()` source. (191158203)
- Fixed content in flex containers being cut off, by reverting a change to the flex base size of items with `min-width` or `max-width`. (191245011)

#### Deprecations

- Removed the non-standard `percentage` value from `-webkit-line-clamp`. (159808285)
- Removed `margin-trim` support from grid containers, following the CSSWG resolution limiting it to block and multi-column containers. (184164505)

### Canvas

#### Resolved Issues

- Fixed the canvas `font` keywords `larger` and `smaller` scaling by 1.02 instead of approximately 1.2. (184312611)
- Fixed `isPointInPath()`, `isPointInStroke()`, and transform methods on a canvas with zero width or height returning wrong results or being ignored. (185387739)
- Fixed an issue where a placeholder `<canvas>` element with no pushed `OffscreenCanvas` frame would fail instead of returning a transparent black image. (186229685)
- Fixed an issue where an off-by-one error in the bottom-row check caused canvas noise injection to misclassify the bottom-left pixel. (186640624)
- Fixed a performance regression where drawing a canvas onto itself with `drawImage` prevented its backing surface from being recycled. (186731221)
- Fixed an issue where a canvas 2D context remained unusable after a temporary failure to allocate its backing store. (186799597)
- Fixed an issue where drawing to `<canvas>` computed path bounds unnecessarily when the whole backing store was already marked dirty. (186946552)
- Fixed a WebGL regression with texture uploads that specify a format and type. (190047059)

### DOM

#### Resolved Issues

- Fixed the realm of nodes to match the DOM Standard, including when a node is adopted into another document or its frame is removed. (182513680)
- Fixed `document` named property lookup for nested `<object>` and `<embed>` elements so it matches `Object.getOwnPropertyNames(document)`. (185692850)
- Fixed `window.open()` with `noopener` setting an opener on a reused window and returning `null` instead of the window when targeting `_self`. (185957071)
- Fixed cloned documents losing their opt-in to declarative shadow roots, and fixed documents from `Document.parseHTMLUnsafe()` having an opaque origin. (186535718)

### Editing

#### Resolved Issues

- Fixed an issue that  disallowed font names that were not a valid CSS identifiers. (51409819)
- Fixed aborting a dead key composition not firing `compositionend`, or firing it with empty `data` instead of the dead key character. (166881240)
- Fixed choosing a spelling suggestion firing input events with `inputType` set to `insertText` instead of `insertReplacementText`. (166940428)
- Fixed typing a space in editable content inside a `<summary>` or `<button>` element also activating that element. (185479319)
- Fixed an issue on macOS where the Copy option was enabled in the edit menu after selecting text in a PDF that disallows copying. (186648332)

### Forms

#### Resolved Issues

- Fixed an issue where the `datalist` popup menu was presented in the wrong place on a screen to the left of the main screen. (181967418)
- Fixed `<select multiple>` on iOS not updating its button text when the selection changes. (185150121)
- Fixed dragging the thumb of a vertical or transformed `<input type="checkbox" switch>` toggling it at the wrong position. (185284079)
- Fixed the thumb of `<input type="checkbox" switch>` being tinted while pressed on macOS. (185957232)
- Fixed only one new window opening when a page submitted several forms or followed several links with `target="_blank"` in a row. (186253237)
- Fixed `ElementInternals`’s `setValidity()` not normalizing newlines in the validation message the way `setCustomValidity()` does. (186355497)
- Fixed email address AutoFill suggestions remaining visible after a page hides the text field.  (186460446)
- Fixed search fields missing their magnifying glass icon. (188825692)
- Fixed customizable `<select>` picking an option on `mousedown` and `keypress`, so you can now press, drag to an option, and release to choose it. (188830823)
- Fixed `<select>` to update every `<selectedcontent>` element it contains, not just the first one, to match the updated HTML specification. (189041604)
- Fixed `<optgroup>` labels so only a `<legend>` that is the first element child is used, falling back to the `label` attribute, to match the HTML specification. (189042427)
- Fixed an `<option>` being chosen by its access key when it is disabled. (189042890)
- Fixed picking an option in an `appearance: base-select` picker to set its dirtiness and to not pick in a disabled `<select>`. (189043002)
- Fixed `<selectedcontent>` not updating when the user picked an option in a single-select list box. (189043051)
- Fixed `<select>` computing the style of its selected option from outdated ancestor styles. (189167314)
- Fixed creating a `<select>` triggering a Content Security Policy `style-src` violation. (190641471)

### HTML

#### New Features

- Added support for the `Origin-Agent-Cluster` header. `document.domain` remains accessible by default, and the header can be used to disable it. (182112072)
- Added support for the `headingoffset` and `headingreset` attributes. (182180043)
- Added support for `popover=hint`. (184548373)
- Added support for the `interactive-widget` key in the viewport `<meta>` tag, with the values `resizes-visual`, `resizes-content`, and `overlays-content`, to control how the page responds when the on-screen keyboard appears. (184654901)

#### Resolved Issues

- Fixed a color input with `display: none` not opening when its `<label>` is clicked. (100476630)
- Fixed CDATA sections not being allowed at integration points during fragment parsing. (182349692)
- Fixed the HTML parser building invalid DOM trees when script moved elements into another document, a shadow root, or a `<template>` while the page was still being parsed. (183256491)
- Fixed a `<label>` default action triggering when clicked interactive content removes itself. (184381262)
- Fixed clicking an element nested inside a checkbox or radio input wrongly activating the ancestor input. (184441087)
- Fixed focus not being restored to the correct element when a `<dialog>` is closed. (184751412)
- Fixed confirming an IME composition removing its containing positioned element. (184918934)
- Fixed the dialog focusing steps not moving focus after calling `show()` because the `<dialog>` was still treated as unrendered. (185156091)
- Fixed `dialog.close()` restoring focus even when focus was not inside the dialog and the dialog was not modal. (185549474)
- Fixed `documentElement.focus()` to move focus to the viewport instead of doing nothing. (185567540)
- Fixed the HTML parser inserting an element into its own subtree when a custom element’s constructor moved the element’s parent into a shadow root or a `<template>` during parsing. (185861243)
- Fixed script elements parsed from XML by `DOMParser` executing after being cloned. (185943138)
- Fixed content placed outside a misnested `<table>` being inserted in the wrong place, or dropped, when script moved the table while the page was still being parsed. (186340113)
- Fixed setting `innerHTML` on a `<template>` inside a `<form>` dropping nested `<form>` elements from the parsed content. (186888019)
- Fixed setting `innerHTML` on SVG or MathML elements dropping NULL characters at the start of the content instead of replacing them with U+FFFD, and treating a leading CDATA section as a comment. (187185909)
- Fixed NULL characters being dropped instead of replaced with U+FFFD when setting `innerHTML` on elements such as `<textarea>`, `<title>`, and `<style>`. (187277178)

### Images

#### Resolved Issues

- Fixed an `<img>` showing an SVG with `height="0"`, a `viewBox`, and no width filling its container instead of rendering at zero width. (186891076)

### JavaScript

#### New Features

- Added support for `Iterator.prototype.includes()`. (173846280)
- Added support for Explicit Resource Management, including `Symbol.dispose`. (180966970)
- Added support for `Temporal`, a modern API for working with dates and times. (181723535)
- Added support for deferred module evaluation with `import defer`. (183892394)
- Added support for `Iterator.prototype.join()`. (183892495)
- Added support for iterator chunking, including `Iterator.prototype.chunks()` and `Iterator.prototype.windows()`. (183892687)
- Added support for the joint iteration proposal, including `Iterator.zip()` and `Iterator.zipKeyed()`. (183892768)
- Added support for importing text modules with an import attribute of `type: text`. (184443879)
- Added support for `BigInt` values in `Intl.PluralRules.prototype.select` and `Intl.PluralRules.prototype.selectRange`. (186534585)

#### Resolved Issues

- Fixed `worker.terminate()` and page reloads not terminating a worker that is blocked in `Atomics.wait` or a WebAssembly `atomic.wait`. (147482360)
- Fixed an issue in JavaScriptCore where a stale inline cache for a custom accessor on a previously flattened dictionary could persist after the accessor was shadowed, which could cause code that replaces built-in properties at runtime (such as a test mocking library overriding `XMLHttpRequest`) to keep using the original value. (180048596)
- Fixed an issue where `Intl.DurationFormat` in `digital` style included a stray separator when `minutesDisplay` was set to `"auto"` and minutes ended up hidden. (180722012)
- Fixed JavaScript module imports that failed with an HTTP or network error being cached, so a later `import()` of the same module can now retry. (182908208)
- Fixed the `String.prototype.localeCompare()` collator cache going stale after a language change. (184096794)
- Fixed `Array.prototype.sort()` not being stable when called without a comparator. (184189734)
- Fixed global object attribute getters and setters throwing when called as bare functions from global scope. (184273476)
- Fixed `Iterator.prototype.chunks()` and `Iterator.prototype.windows()` to match the latest specification. (184321801)
- Fixed `Intl.Locale` collections not being sorted. (184322384)
- Fixed `formatToParts()` omitting the era separator that `format()` inserts. (184382546)
- Fixed the `import defer` implementation to match the updated proposal. (184423667)
- Fixed an issue where `Array.prototype.toSpliced` threw a `TypeError` instead of a `RangeError` when the array’s length was `Infinity`. (184438837)
- Fixed `\P{...}` on the right side of a `v` mode `&&` or `--` operation being treated as a union. (184443379)
- Fixed non-ISO calendar date field resolution at the edges of the supported range. (184478785)
- Fixed a regular expression string-list alternative containing a non-BMP character matching on only its leading code units. (184582034)
- Fixed the `WebAssembly.Global` `value` setter not treating a missing argument as `undefined`. (184608074)
- Fixed Unicode property escapes ignoring case-insensitive matching in `u` and `v` modes. (184762230)
- Fixed the Before Hijra era year being computed from rendered text instead of the calendar. (184853584)
- Fixed `Promise.try()` to resolve its result with `PromiseResolve`, so a promise returned by the callback is no longer wrapped in an extra promise. (185064567)
- Fixed the `Referer` header sent for descendant and dynamically imported module script fetches. (185943042)
- Fixed `String.prototype.replace` with a unicode regular expression splitting a surrogate pair after an empty match. (186143674)
- Fixed an issue where `TypedArray` `setFromTypedArray` could not use `memmove` when the region was intentionally overlapping and the spec algorithm needed to read back the modified result. (186145219)
- Fixed an issue where the `TypedArray` constructor could produce incorrect results when copying `Array` content whose element access has side effects. (186227333)
- Fixed an issue where a character following a class set operand in a `/v` mode regular expression class incorrectly added `U+0000` to the class. (186319779)
- Fixed an issue where `Object.freeze()` did not invalidate the megamorphic inline cache epoch, which could cause stale property accesses on a frozen object. (186393610)
- Fixed an issue where deleting a property of a dictionary prototype in place did not invalidate the megamorphic store cache. (186513123)
- Fixed an issue where regular expression lookbehind assertions could fail to match, or match at an invalid position, due to incorrect handling of surrogate pairs in the regular expression interpreter. (186536137)
- Fixed an issue where `Atomics.isLockFree()` converted its argument with a 32-bit integer conversion instead of `ToIntegerOrInfinity`, which could cause it to incorrectly return `true` for large size values. (186610789)
- Fixed an issue where a JIT fast path for `RegExp.prototype.test` could skip the required read of `lastIndex`, silently dropping observable side effects. (186792229)
- Fixed an issue where tail-call optimization was skipped for `eval` calls that didn’t resolve to the real `eval` function, and incorrectly applied inside generator and async function bodies, which could produce incorrect results. (186840477)
- Fixed an issue where `RegExp.escape` incorrectly narrowed supplementary code points to 16 bits. (186962453)
- Fixed an issue where a `\-` following a class set operand in a `/v` mode regular expression class incorrectly threw a `SyntaxError`. (186962513)
- Fixed an issue where `RegExp::deleteCode()` cleared a regular expression’s cached pattern atom, which could cause incorrect values from static `RegExp` properties such as `leftContext` and `rightContext` after the compiled code was reclaimed while idle. (187104089)
- Fixed an issue where `String.prototype.at` and `String.prototype.codePointAt` could return an incorrect value for an out-of-bounds or negative index because the JIT compiler could eliminate their bounds check. (187336661)

### MathML

#### Resolved Issues

- Fixed an issue where U+2016 (DOUBLE VERTICAL LINE) was missing the symmetric property in the MathML operator dictionary. (179558196)

### Media

#### New Features

- Added support for `HTMLMediaElement.removeTextTrack()`. (183365541)

#### Resolved Issues

- Fixed garbled audio when playing WebM files that use `BlockGroup` elements instead of `SimpleBlock` elements. (158943997)
- Fixed videos immediately exiting fullscreen back to inline after an earlier video had been played in fullscreen. (174807377)
- Fixed an issue where interacting with the inline media controls could dismiss a site’s custom video presentation. (181244652)
- Fixed an issue where finding text starting from a selection could resolve to the wrong caption cue instead of the one nearest the video’s playhead. (182001231)
- Fixed video failing with `MEDIA_ERR_ABORTED` and restarting from the beginning after restoring a page from the back/forward cache. (183119720)
- Fixed `requestFullscreen()` and `requestPictureInPicture()` not consuming user activation. (183621577)
- Fixed `MediaRecorder` dropping pending video frames when recording is stopped. (183975207)
- Fixed the auto position of a WebVTT cue with `start` or `end` text alignment to be 50%. (184039946)
- Fixed `MediaRecorder` dropping a frame whenever the writer input reports that it is not ready. (184271782)
- Fixed an issue where wireless playback could create a remote media session helper too eagerly, which could delay switching an active playback route to a wireless device. (184536781)
- Fixed an issue where `MediaRecorder` could hold back a lone video keyframe indefinitely instead of using it to start a new recording segment. (186229843)
- Fixed an issue where black video-range pixel buffers were produced with super-black values instead of legal black. (187309125)
- Fixed the `play()` promise not resolving for MSE content when the FairPlay content key is already known. (188022794)
- Fixed the WebCodecs H.264 encoder buffering too many frames. (188201578)
- Fixed video disappearing when returning from Picture-in-Picture to element fullscreen and then inline on iOS. (188256091)
- Fixed paused video starting to play again without user interaction in a hidden or minimized window. (188824968)
- Fixed WebCodecs VP8, VP9, and AV1 encoders encoding uninitialized data for 10-bit frames. (189532957)
- Fixed Media Source Extensions playback permanently stalling after a video track is flushed. (190456521)
- Fixed swiping down a fullscreen video putting it into mini-player mode. (191046166)
- Fixed `readyState` not returning to `HAVE_METADATA` when seeking to an unbuffered range, which paused video while scrubbing. (191310594)

### Navigation API

#### New Features

- Added support for the `to` property on `NavigationTransition`. (184792753)
- Added support for intercepting a navigation with a precommit handler. (184893603)

#### Resolved Issues

- Fixed `sourceElement` reporting the deepest clicked element instead of the element responsible for the navigation. (184581613)
- Fixed `NavigationHistoryEntry` returning `null` instead of the empty string for `url`, `key`, and `id` when the document is not fully active. (184590003)
- Fixed `navigation.activation.from` not being `null` when navigating away from the initial `about:blank`. (184624752)
- Fixed `navigateerror` not firing for a navigation started from a `navigateerror` handler. (184633618)

### Networking

#### New Features

- Added support for streaming request bodies in `fetch()` by passing a `ReadableStream` as the `body`. (183714274)

#### Resolved Issues

- Fixed `application/json` responses with no `charset` showing garbled text when displayed in a frame, by decoding them as UTF-8. (71522231)
- Fixed a same-frame fragment navigation cancelling a download started by a `download` attribute click in the same task. (165498647)
- Fixed `<link rel=preload as>` keywords not being matched ASCII case-insensitively. (184013239)
- Fixed CORS preflight requests hanging indefinitely when the server’s `OPTIONS` response body never finished, by deciding the preflight from the response headers. (184231090)
- Fixed PDF byte-range requests being blocked by the `connect-src` Content Security Policy directive instead of `object-src`. (184258237)
- Fixed a Content Security Policy `host-source` of the form `*:*/path` not matching. (184902666)
- Fixed a policy decision that outlives its navigation being applied to an unrelated load. (184974939)
- Fixed cookies being stored as session cookies when their `Expires` date uses the month-before-day format produced by `Date.prototype.toString()`. (185840799)
- Fixed parsing of `Range` header values for `blob:` URLs and CORS-safelisted requests to match the Fetch Standard. (186856678)
- Fixed an issue where reading a file-backed `Blob` range larger than 2GB truncated the read length due to an integer overflow. (187207663)
- Fixed an issue where validation of an HTTP header value did not check its final character, allowing control characters and DEL to be accepted as valid. (187288970)
- Fixed failed speculative prefetches causing the actual navigation to fail. (188633133)
- Fixed non-ASCII `Last-Event-ID` request header values being UTF-8 encoded twice, including for `EventSource` reconnects through a redirect. (190165073)
- Fixed the third-party IP address cloaking defense capping the lifetime of cookies set by `google.com` subdomains. (191056176)

### Performance

#### Resolved Issues

- Fixed hidden page throttling heuristics not being applied to newly created pages. (185461584)
- Fixed excessive CPU and power usage caused by `IntersectionObserver` observation on pages with many observed elements. (185839711)
- Fixed an issue where style resolution for elements sharing a `scroll-timeline` name could block the main thread for multiple seconds. (186090970)
- Fixed an issue where `ScrollingStateTree::insertNode` performed redundant work reordering children on pages with many sibling scrolling nodes. (186143008)
- Fixed an issue where ordinary property changes, such as toggling `overflow: hidden`, could trigger an unnecessary full-layer repaint. (186422878)

### Rendering

#### New Features

- Added support for dark mode in the XML document viewer. (122234600)
- Added Adaptive Dark Mode, which automatically adapts bright web pages that don’t natively support dark mode, giving users an optimized viewing experience when browsing at night or in dark environments.  (189226811)

#### Resolved Issues

- Fixed text selection highlighting extending incorrectly when a float precedes the text. (109610452)
- Fixed an issue where a layer with a negative `z-index` inside a stacking context failed to composite correctly when overlapping an externally composited layer. (130595406)
- Fixed text underlines rendering incorrectly for Urdu text. (161299983)
- Fixed an issue where `box-shadow` rendering broke when the page was zoomed. (169167365)
- Fixed an issue where the `<mo>` operator dictionary was consulted even when the element contained non-text content. (173078723)
- Fixed characters overlapping adjacent text when a space glyph’s base advance is substituted. (180227130)
- Fixed incorrect element dimensions being reported for content inside an `iframe` whose owner element generates no box. (181639379)
- Fixed content overlapping when an element gains a scrollbar during layout. (183465635)
- Fixed Arabic letters in adjacent inline boxes not being joined. (184071471)
- Fixed a self-collapsing block nested in an inline box losing its margin when the root has a border. (184145672)
- Fixed trailing whitespace not being collapsed before a block nested in an inline box. (184151239)
- Fixed baseline alignment ignoring the offset of a block level box nested in an inline box. (184153324)
- Fixed an empty orthogonal block nested in an inline box stretching the line. (184158817)
- Fixed the margin after a block level box on a line being lost on relayout. (184159645)
- Fixed an empty editable container with only an out-of-flow child losing its line. (184176269)
- Fixed a float inside a block nested in an inline box intruding at the wrong position. (184184683)
- Fixed the baseline of an inline-block whose last line box holds a block level box dropping that line’s offset. (184222186)
- Fixed nested inline boxes around a block level box being stretched by their nesting depth. (184222677)
- Fixed an inline box with cloned decorations generating an extra line between two block level boxes. (184241600)
- Fixed a block whose content is a table being treated as self-collapsing. (184337051)
- Fixed a block level box’s margin after being counted twice when only that box needs layout. (184344633)
- Fixed an outside list marker making its list item’s children inline. (184380304)
- Fixed an excluded list marker aligning with a block level box on a line instead of the first line of text. (184405037)
- Fixed text autosizing on iOS enlarging text too much when a block-level box sits on the same line as text. (184505321)
- Fixed a block level box on a line reporting its scrollable overflow at its static position. (184505703)
- Fixed a block level box on a line not starting a new paragraph for `unicode-bidi: plaintext` and `text-indent: each-line`. (184505835)
- Fixed a highlight on the line after a block level box covering the box’s margin. (184506039)
- Fixed a block level box on a line switching off `text-wrap: balance` for the whole container. (184508888)
- Fixed inline boxes that are not relatively positioned offsetting their out-of-flow children by the position of the line. (184512485)
- Fixed a block level box on a line not contributing its margin box to its container’s overflow. (184526625)
- Fixed list-based hit testing reporting the container before a block level box on an earlier line. (184527135)
- Fixed selection gaps not being filled around a block level box on a line. (184527621)
- Fixed a forced page break after a block level box on a line not moving the following content to the next page. (184712866)
- Fixed a float not being offered to the caret when its container has a block level box on a line. (184713698)
- Fixed a `<fieldset>` on a line taking its legend’s overhang twice. (184714637)
- Fixed a `visibility: visible` child with `overflow: hidden` staying hidden inside a positioned `visibility: hidden` parent. (184801325)
- Fixed a box that collapsed through with clearance on a line pushing the following content down by its margin. (184917509)
- Fixed intrinsic width computation when a line holds a block level box. (184968113)
- Fixed a list marker overlapping the list item content when the marker text is right-to-left. (185048387)
- Fixed an outside list marker keeping a line of its own when a block is appended to an empty list item. (185109123)
- Fixed a block-level box on a line being handed its own float as an intruding float. (185109160)
- Fixed list markers not updating when the list item’s font changes dynamically. (185330733)
- Fixed an issue where adjoining margins did not collapse when a container’s first child was a float or an out-of-flow box. (185591842)
- Fixed an issue where margins did not collapse after a self-collapsing block-level box on a line. (185598333)
- Fixed an issue where a list marker was painted on top of the list item’s content instead of behind it. (185741211)
- Fixed an issue where a block-level box on a line was left behind when a column break moved the line. (185787568)
- Fixed an issue where a `max-width` length was not honored on an out-of-flow replaced element with an intrinsic aspect ratio. (185831651)
- Fixed a relatively positioned block-level box on a line reporting scrollable overflow as wide as the entire line. (185835450)
- Fixed an issue where an orthogonal block-level box inside an inline box made its container as wide as the box instead of as wide as its content. (185890940)
- Fixed the position of an orthogonal block-level box inside an inline box. (185895981)
- Fixed `background-size: cover` painting nothing for an SVG image with an extreme natural aspect ratio. (186006463)
- Fixed a regression that caused extra spacing to appear between an image and surrounding content near the bottom of a page. (186102748)
- Fixed an issue where text nodes inside a `display: contents` element received redundant updates during style resolution. (186246705)
- Fixed an issue where content changing inside an element with a `blur()` filter did not properly repaint, leaving stale pixels around the edge of the filtered region. (186278957)
- Fixed an issue where a MathML `rowspan="0"` attribute was incorrectly clamped to 1. (186420659)
- Fixed an issue where non-MathML children of `<annotation>` and `<annotation-xml>` were not rendered. (186429768)
- Fixed an issue where drawing a native image did not respect the requested `InterpolationQuality`, affecting image scaling across canvas, SVG, and PDF rendering paths. (186439811)
- Fixed an issue where a layer with `clip-path` or `mask` could be treated as fully opaque, causing incorrect rendering. (186722177)
- Fixed an issue where a `position: sticky` element with `-webkit-box-reflect` applied could composite its reflection incorrectly. (186812790)
- Fixed text in the Best Buy Apple Pay button rendering inverted, by reverting a change to how glyphs are drawn. (187741746)

### SVG

#### New Features

- Added support for `text-overflow` as an SVG presentation attribute. (176146717)
- Added support for `fill` and `stroke` referencing paint servers in external SVG documents. (181031373)
- Added support for SVG external resources, allowing `url()` references to SVG resources such as filters, masks, and gradients in external documents. (183940963)
- Added support for the SVG 2 `path` attribute on `<textPath>`, which lets text follow an inline path without referencing a separate `<path>` element via `href`. (185831618)

#### Resolved Issues

- Fixed an issue where SVG conditional processing attributes on `clipPath`, `mask`, and `pattern` elements incorrectly prevented the resource from being referenced. (19103270)
- Fixed an issue where SVG number attributes did not revert to their initial value when removed or set to an invalid value. (165378154)
- Fixed `SVGSVGElement.currentScale` being a no-op on an outermost `<svg>` that is not the document root. (180889449)
- Fixed a `clip-path` basic shape being mispositioned on a `<foreignObject>` with a non-zero `x` or `y`. (182755161)
- Fixed changes to the `href` of an SVG `<image>` not updating the `<use>` elements that reference it. (183402463)
- Fixed a `clip-path` basic shape being mispositioned on a rotated or scaled SVG element. (184494108)
- Fixed `<animateMotion>` ignoring a zero-length motion path. (184569273)
- Fixed an issue where a SMIL animation of a presentation attribute was never released after the animated element was detached from the document, permanently freezing the animated value. (185452156)
- Fixed an issue where `SVGLength` resolved `ex` units by rounding the font’s x-height up to a whole pixel, causing the SVG DOM and `getComputedStyle` to disagree. (185984854)
- Fixed an issue where additive color animations in SVG lost precision due to per-layer 8-bit rounding. (186223510)
- Fixed an issue where an SVG transform change could leave an ancestor layer’s cached repaint rects stale, resulting in incorrect repainting. (187005898)
- Fixed tearing down SMIL animation correctly even if its target element or its attribute name changes in a reentrant code.  (189708246)
- Fixed removing or retargeting an active `<animateMotion>` leaving its previous target in an animated state. (191240656)

#### Deprecations

- Removed the `use-script`, `no-change`, and `reset-size` values from `dominant-baseline` to match SVG 2. (174635806)

### Scrolling

#### Resolved Issues

- Fixed an issue where re-snapping did not select the snap area aligned in both axes when multiple targets were aligned. (182285397)
- Fixed an issue where `scroll-snap-align` was not respected when scrolling to an anchor or calling `scrollIntoView()`. (182544180)
- Fixed `element.scroll()` and `element.scrollTo()` not scrolling inside a `content-visibility: hidden` subtree. (184935071)

### Security

#### New Features

- Added support for viewing 2-QWAC certification information for a webpage.  (166719646)

#### Resolved Issues

- Fixed an issue where navigations to external URLs in subframes were not consistently blocked. (185801936)
- Fixed an issue where `CredentialStorage::removeCredentialsWithOrigin` failed to purge HTTPS credentials that used the default port. (187210150)

### Spatial Web

#### New Features

- Added preview support for Spatial CSS Portals and Connected Volumetric Scenes in visionOS. To preview, enable the *Spatial CSS Portals* feature in Settings.  (182292632)

#### Resolved Issues

- Fixed an issue where the background color of `HTMLModelElement` did not match spec for non-opaque colors. (181641249)

### Web API

#### New Features

- Added support for `QuotaExceededError` as a `DOMException` subclass, exposed on `window` and worker global scopes. (141586555)
- Added support for subgroups in WebGPU. (154874391)
- Added support for close watchers and the `closedby` attribute for `dialog` elements. (180105698)
- Added support for requesting OpenID4VP credentials with the Digital Credentials API.  (180867795)
- Added support for `getAllRecords()` and `IDBGetAllOptions` in IndexedDB. (181043154)
- Added support for serializing and storing `FileSystemHandle` objects. (182178736)
- Added support for creating dedicated workers from shared workers. (182181082)
- Added support for a `stack` property on `DOMException`, matching other error objects. (185770735)

#### Resolved Issues

- Fixed an issue where `scrollWidth` and `clientWidth` returned inconsistent values when the page was zoomed in or out due to rounding. (121879134)
- Fixed a missing `resize` event when an iframe transitions from `display: none` to visible. (174638256)
- Fixed an issue where a user gesture authorization token was not properly verified for Digital Credentials requests. (174908839)
- Fixed an issue where Scroll To Text Fragment directives could run outside `text/html` and `text/plain` documents. (181763736)
- Fixed an issue where `replaceChildren()` could not replace a document’s children. (181921026)
- Fixed exceptions in workers, including script parse errors, not being reported correctly. (182111908)
- Fixed the Digital Credentials API settling the `navigator.credentials.get()` promise synchronously instead of queuing a global task as required by the specification. (182678875)
- Fixed `getBoundingClientRect()` returning a non-zero rect for SVG elements inside hidden containers. (183425103)
- Fixed several `URLPattern` matching issues affecting Service Worker routing, including incorrect encoding of the `username` and `password` components and unhandled unclosed pattern groups. (183434701)
- Fixed an issue where WebDriver reported an empty URL instead of `about:blank` for a browsing context that had not yet navigated. (183468933)
- Fixed reentrant custom element construction by implementing the active custom element constructor map. (184050659)
- Fixed fullscreen state not being unwound when entering fullscreen fails. (184157871)
- Fixed the `SharedWorkerGlobalScope` prototype not being an immutable prototype exotic object. (184190755)
- Fixed the `scrollend` event not firing when wheel-scrolling a subframe. (184352772)
- Fixed `DataTransfer.getData("url")` returning the whole `text/uri-list` instead of only its first URL. (184988378)
- Fixed `DataTransferItem.kind` to return an empty string once the item is no longer part of an active drag data store. (185010027)
- Fixed a streaming `fetch()` response body being withheld from the reader until the next network chunk arrived. (185883588)
- Fixed an issue where `Cache.delete()` and `Cache.keys()` swallowed exceptions thrown while constructing a `Request` from a URL string. (186636105)
- Fixed a regression where WebXR hit testing failed with a `TypeError` when `offsetRay` was not specified. (186997100)
- Fixed `DataTransferItemList.clear()` removing items when the drag data store is not in read/write mode. (187160061)
- Fixed randomized `navigator.hardwareConcurrency` values in known fingerprinting scripts, which now alternate between 4 and 8. (190053521)
- Fixed “Copy to clipboard” actions not always working the first time after script evaluated on behalf of a client consumed the page’s transient user activation. (190767489)

#### Deprecations

- Removed the non-standard `DataTransferItemList.prototype.item()` method to match the HTML specification; use index access such as `items[0]` instead. (185019165)

### Web Audio

#### Resolved Issues

- Fixed an `AudioWorkletProcessor` being torn down too early after `process()` returns `false`. (184107806)
- Fixed the `AudioWorkletNode` `processorerror` event missing `filename`, `lineno`, and `colno`. (184224032)
- Fixed a zero-duration `exponentialRampToValueAtTime()` at a non-frame-aligned time rendering `NaN`. (184434164)
- Fixed setting `ConvolverNode.buffer` to `null` not releasing the impulse response. (184434803)
- Fixed `AudioBufferSourceNode` ignoring the offset passed to `start()` when using a negative `playbackRate`. (184484940)
- Fixed `AudioBufferSourceNode` to clamp out-of-range `loopStart` and `loopEnd` values. (185752079)
- Fixed an issue where `AudioBufferSourceNode` rendered only silence when `start()` was called with an out-of-bounds offset and a negative `playbackRate`. (185769043)

### Web Extensions

#### New Features

- Added support for `setAccessLevel()` on the `local` and `sync` storage areas. (183680404)
- Added support for the `offscreen` API. (184269255)
- Added support for `scripting.ExecutionWorld`. (184284891)

#### Resolved Issues

- Fixed an issue where `i18n.getMessage()` dropped non-string substitution arguments instead of coercing them to strings. (149855718)
- Fixed an issue where a high priority static declarativeNetRequest redirect rule was not favored over a low priority session redirect rule. (176176246)
- Fixed an issue where `webRequest` events did not fire for loads blocked by a declarativeNetRequest rule. (176177851)
- Fixed an issue where `webRequest` events did not fire for page loads created with `tabs.create`. (177727052)
- Fixed an issue where an extension’s service worker lost its clients after being unloaded and reloaded, preventing it from finding an existing offscreen document. (186116488)

### Web Inspector

#### New Features

- Added support for throttling the network speed of the inspected page. (144892477)
- Added support for the range mappings proposal in source maps. (178564308)
- Added per-element `Layout Invalidated` events in Web Inspector to reflect the number of elements affected by a layout invalidation. (181243589)
- Added support for editing WebGPU shaders in the Canvas tab. (184128414)
- Added support for highlighting WebGPU render pipelines in the Canvas tab. (184169419)
- Improved the estimated memory use of WebGL and WebGPU canvases to include their GPU resources, such as textures and buffers. (184535731)
- Added support for showing object arguments and return values in Canvas recordings. (184759172)
- Added support for showing flag names, such as `GPUBufferUsage.COPY_DST`, instead of raw numbers in WebGPU Canvas recordings. (184928178)
- Added syntax highlighting to actions in Canvas recordings. (184936730)
- Added logging of the site-specific quirks active on a page to the Web Inspector console. (185246801)

#### Resolved Issues

- Fixed Canvas recordings that are no longer in use continuing to hold memory. (35893620)
- Fixed resource search returning duplicate results for the same resource. (42879586)
- Fixed an issue where every `<input>` element showed a Scroll badge in the Elements tab. (101661656)
- Fixed an issue where search results did not select the corresponding source code line for fetched JSON. (118115749)
- Fixed an issue where search in Web Inspector did not find results inside the shadow DOM. (126458322)
- Fixed Find in Page not working in Responsive Design Mode.  (158871569)
- Fixed an issue where Web Inspector could crash when selecting a popover matching a nested `@scope` with a bare declaration. (181745000)
- Fixed an issue where Web Inspector mapped the `crimson` named color to the wrong RGB value. (182090064)
- Fixed an issue where the gradient editor in Web Inspector dropped explicit `0%` color stops and misparsed leading radial color stops. (182172439)
- Fixed an issue where autocompleting a vendor-prefixed value in Styles could duplicate the prefix, for example producing `-apple--apple-system`. (182178871)
- Fixed `file://` resources showing unnamed folders in the Sources tab when grouped by path. (182657742)
- Fixed WebGPU canvases being treated as CSS canvases in the Canvas tab. (184346714)
- Fixed an exception when selecting a CDATA section in the DOM tree. (185027124)
- Fixed `WebSocket` handshake headers sometimes missing from the Network tab. (185255819)
- Fixed scripts from other frames disappearing from the Sources tab when an iframe navigates. (187042936)
- Fixed the Styles panel showing incorrect information for CSS rules that mix nested `@media` rules with declarations. (187701896)
- Fixed the “Request Data” arrow in the Network tab’s Headers view opening the response body instead of the request body. (188816643)
- Fixed the Sources tab showing no scripts when inspecting a device running an older OS. (188830442)
- Fixed Timelines recordings after the first one capturing no data. (189690367)
- Fixed Safari extension content scripts missing from the Sources tab. (190789931)

### WebAssembly

#### New Features

- Added support for relaxed SIMD instructions. (180967232)
- Added support for WebAssembly Memory64. (183543404)

#### Resolved Issues

- Fixed inconsistent `CompileError` messages when compiling a WebAssembly module with more than one invalid function by always reporting the error for the lowest function index. (140651602)
- Fixed a re-exported imported `WebAssembly.Tag` not being the same object as the one that was imported. (185121644)
- Fixed re-exporting an imported immutable `WebAssembly.Global` so that the exports object returns the same object instead of a new wrapper. (185184951)
- Fixed `WebAssembly.Module.imports()` and `WebAssembly.Module.exports()` exposing the `type` field from the unfinished JS Type Reflection proposal. (185281658)
- Fixed an issue where JS string builtins and imported string constants were not applied when compiling WebAssembly modules loaded as ES modules. (186037843)
- Fixed an issue where the `WebAssembly.Exception` constructor rejected `null` options and incorrectly accepted non-object options. (186319813)

### WebCodecs

#### New Features

- Added support for the WebCodecs `ImageDecoder` API. (184857272)

### WebDriver

#### Resolved Issues

- Fixed WebDriver BiDi `script.callFunction` cutting off part of error messages. (186311752)
- Fixed the Delete All Cookies command returning before all cookies were deleted. (186410147)
- Fixed SafariDriver mis-parsing the next request on a keep-alive connection after a `GET` request with a body.  (186496411)
- Fixed WebDriver passing malformed or unknown element and shadow root references to scripts instead of returning an error.  (186602209)
- Fixed WebDriver returning a “stale element reference” error instead of “no such element” for an element from a different browsing context. (186615759)
- Fixed WebDriver reporting “no such element” instead of “no such shadow root” for a shadow root reference from a different browsing context.  (186698241)
- Fixed WebDriver not handling right-side modifier keys, such as `ShiftRight` and `ControlRight`, on Apple platforms. (186961436)
- Fixed the Add Cookie command dropping a cookie that has no `sameSite` attribute. (187193380)
- Fixed WebDriver reporting “no such element” instead of “stale element reference” when a script returns a stale node. (188826494)

### WebGL

#### Resolved Issues

- Fixed an issue where WebGL contexts created with `premultipliedAlpha: false` were composited incorrectly. (53509398)
- Fixed the orientation and improved the performance of WebGL canvas contents copied into an image, such as when drawing a WebGL canvas into a 2D canvas or an `ImageBitmap`. (184913852)
- Fixed `getAttribLocation()` and `getUniformLocation()` not reporting an `INVALID_OPERATION` error when querying an unlinked program with a reserved name prefix. (185565011)

### WebGPU

#### New Features

- Added support for the `snorm10-10-10-2` value of `GPUVertexFormat`. (185379686)

#### Resolved Issues

- Fixed an issue where uploading a `canvas` as a WebGPU texture had very poor performance. (153642354)
- Fixed `GPUQueue.copyExternalImageToTexture()` uploading indexed PNG images incorrectly. (184529653)
- Fixed a GPU hang when a render pass issued repeated `drawIndirect()` or `drawIndexedIndirect()` calls using the same buffer. (185057290)
- Fixed a typo in WGSL diagnostics that named the `sampler_comparison` type incorrectly. (186031593)
- Fixed an issue where `GPUDevice.createBindGroup()`’s fast path failed to reuse bind groups containing a `GPUBuffer` entry alongside an external texture, forcing an unnecessary full rebuild. (186379208)
- Fixed an issue where a WebGPU external texture imported from a `video` element using WebM or MSE playback rendered as a black placeholder instead of the video frame. (186470526)
- Fixed an issue where using WebGPU render bundles on some GPUs could cause the device to be unexpectedly lost. (186688781)
- Fixed an issue where WebGPU could report the `primitive-index` feature as available on GPUs that don’t support it, resulting in an uncaptured error. (186690340)
- Fixed an issue in WebGPU where an array value constructor referenced through a type alias could generate invalid Metal Shading Language, silently producing incorrect compute results. (186803296)
- Fixed an issue in WebGPU where inlining three or more calls to a function operating on a large struct could silently miscompile on some devices, producing incorrect results. (186804865)
- Fixed an issue where asynchronous pipeline creation could stall rendering. (187296614)

### WebKit API

#### Resolved Issues

- Fixed `WebPage.backForwardList` in the SwiftUI WebKit API not reflecting navigations, so the list now updates reliably and changes to it can be observed. (184634983)
- Fixed an issue where `WKWebView.magnification` reported the pre-gesture scale for a few moments after a pinch-to-zoom gesture ended, instead of the scale about to commit. (185381317)

### WebRTC

#### New Features

- Added WebRTC AV1 software fallback support. (182789617)

#### Resolved Issues

- Fixed TURN server URLs containing query-string parameters such as `?transport=tcp` being rejected, which prevented relay ICE candidates from being gathered. (184556197)
- Fixed 8-bit YUV 4:2:2 VP9 frames from the software decoder being converted with the U and V planes swapped. (189584834)

### XML

#### Deprecations

- Added a console warning when a document declares an XML external entity. (190488621)

## See Also

### Version 27
- [Safari 27.2 Release Notes](./safari-27_2-release-notes.md)
  Released October 26, 2026 — 27.2 (20625.2.8)
- [Safari 27.1 Release Notes](./safari-27_1-release-notes.md)
  Released October 23, 2026 — 27.1 (20625.1.29)
- [Safari 27 Release Notes](./safari-27-release-notes.md)
  Released September 14, 2026 — 27.0 (20625.1.29)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-27_3-release-notes)*