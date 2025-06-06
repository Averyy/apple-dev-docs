# UITextSearchingFindSession

**Framework**: UIKit  
**Kind**: class

A find session object that wraps a searchable object implementing the text-searching protocol.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITextSearchingFindSession
```

#### Overview

Implement the [`UITextSearching`](uitextsearching-53wjq.md) protocol on the class that encapsulates the searchable content for your view to use an instance of [`UITextSearchingFindSession`](uitextsearchingfindsession.md) as the session object. Alternatively, you can subclass [`UIFindSession`](uifindsession.md) to manage the details of the session using a custom class.

The find session’s reference to [`searchableObject`](uitextsearchingfindsession/searchableobject.md) is weakly held to avoid a retain cycle if the view you install the interaction on is the searchable object itself. Ensure that your app maintains a strong reference to the searchable object.

## Topics

### Creating a text searching find session
- [init(searchableObject: any __UITextSearching)](uitextsearchingfindsession/init(searchableobject:)-9zc4e.md)
  Initializes an object to manage the search for the searchable object you specify.
- [convenience init<SearchableObject>(searchableObject: SearchableObject)](uitextsearchingfindsession/init(searchableobject:)-7swl5.md)
  Initializes an object to manage the search for the searchable object you specify.
### Getting the searchable object
- [var searchableObject: (any __UITextSearching)?](uitextsearchingfindsession/searchableobject.md)
  The object to search, responsible for performing the search operation and decorating the results.

## Relationships

### Inherits From
- [UIFindSession](uifindsession.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIFindInteraction](uifindinteraction.md)
  An interaction that provides text finding and replacing operations using a system find panel.
- [protocol UIFindInteractionDelegate](uifindinteractiondelegate.md)
  A delegate object that provides a session object to manage the search state for a find interaction and receives notifications of search session lifetimes.
- [class UIFindSession](uifindsession.md)
  An abstract base class that manages the state, presentation, and behavior for a search that the find interaction initiates.
- [protocol UITextSearching](uitextsearching-3wkjv.md)
  The methods you use on a find session’s searchable objects to perform search operations and decorate the found text results.
- [class UITextSearchOptions](uitextsearchoptions.md)
  An object containing the configurable options for a text search.
- [enum UITextSearchFoundTextStyle](uitextsearchfoundtextstyle.md)
  Constants that describe the style a find session uses to decorate the text.
- [UITextSearchOptions.WordMatchMethod](uitextsearchoptions/wordmatchmethod-swift.enum.md)
  Constants that describe the method to use when searching text for words that match a string.
- [UIFindSession.SearchResultDisplayStyle](uifindsession/searchresultdisplaystyle-swift.enum.md)
  Constants that describe the results summary the find panel UI includes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearchingfindsession)*