# UITextSearchOptions.WordMatchMethod

**Framework**: UIKit  
**Kind**: enum

Constants that describe the method to use when searching text for words that match a string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
enum WordMatchMethod
```

## Topics

### Constants
- [UITextSearchOptions.WordMatchMethod.contains](uitextsearchoptions/wordmatchmethod-swift.enum/contains.md)
  The word contains the search string.
- [UITextSearchOptions.WordMatchMethod.startsWith](uitextsearchoptions/wordmatchmethod-swift.enum/startswith.md)
  The word contains the search string as a prefix.
- [UITextSearchOptions.WordMatchMethod.fullWord](uitextsearchoptions/wordmatchmethod-swift.enum/fullword.md)
  The word matches the search string exactly.
### Initializers
- [init?(rawValue: Int)](uitextsearchoptions/wordmatchmethod-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

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
- [enum UITextSearchFoundTextStyle](uitextsearchfoundtextstyle.md)
  Constants that describe the style a find session uses to decorate the text.
- [UIFindSession.SearchResultDisplayStyle](uifindsession/searchresultdisplaystyle-swift.enum.md)
  Constants that describe the results summary the find panel UI includes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearchoptions/wordmatchmethod-swift.enum)*