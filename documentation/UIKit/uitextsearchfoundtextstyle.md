# UITextSearchFoundTextStyle

**Framework**: UIKit  
**Kind**: enum

Constants that describe the style a find session uses to decorate the text.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
enum UITextSearchFoundTextStyle
```

#### Overview

Use [`UITextSearchFoundTextStyle`](uitextsearchfoundtextstyle.md) to identify ranges of text your app decorates to indicate matches, highlighted matches and non-matching text.

## Topics

### Constants
- [UITextSearchFoundTextStyle.normal](uitextsearchfoundtextstyle/normal.md)
  A style that indicates the text isn’t a match.
- [UITextSearchFoundTextStyle.found](uitextsearchfoundtextstyle/found.md)
  A style that indicates the text is a match, but not highlighted.
- [UITextSearchFoundTextStyle.highlighted](uitextsearchfoundtextstyle/highlighted.md)
  A style that indicates the text is a highlighted match.
### Initializers
- [init?(rawValue: Int)](uitextsearchfoundtextstyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class UIFindInteraction](uifindinteraction.md)
  An interaction that provides text finding and replacing operations using a system find panel.
- [protocol UIFindInteractionDelegate](uifindinteractiondelegate.md)
  A delegate object that provides a session object to manage the search state for a find interaction and receives notifications of search session lifetimes.
- [class UIFindSession](uifindsession.md)
  An abstract base class that manages the state, presentation, and behavior for a search that the find interaction initiates.
- [class UITextSearchingFindSession](uitextsearchingfindsession.md)
  A find session object that wraps a searchable object implementing the text-searching protocol.
- [protocol UITextSearching](uitextsearching-3wkjv.md)
  The methods you use on a find session’s searchable objects to perform search operations and decorate the found text results.
- [class UITextSearchOptions](uitextsearchoptions.md)
  An object containing the configurable options for a text search.
- [UITextSearchOptions.WordMatchMethod](uitextsearchoptions/wordmatchmethod-swift.enum.md)
  Constants that describe the method to use when searching text for words that match a string.
- [UIFindSession.SearchResultDisplayStyle](uifindsession/searchresultdisplaystyle-swift.enum.md)
  Constants that describe the results summary the find panel UI includes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearchfoundtextstyle)*