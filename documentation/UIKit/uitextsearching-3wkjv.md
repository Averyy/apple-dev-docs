# UITextSearching

**Framework**: UIKit  
**Kind**: protocol

The methods you use on a find session’s searchable objects to perform search operations and decorate the found text results.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
protocol UITextSearching : NSObjectProtocol
```

#### Overview

Implement this protocol on the class that encapsulates the searchable content for your view. This allows you to use an instance of [`UITextSearchingFindSession`](uitextsearchingfindsession.md) to manage the session for a find interaction.

## Topics

### Handling searches
- [func performTextSearch(queryString: String, options: UITextSearchOptions, resultAggregator: UITextSearchAggregator<Self.DocumentIdentifier>)](uitextsearching-3wkjv/performtextsearch(querystring:options:resultaggregator:).md)
  Searches for ranges of text matching the string across all searchable documents and collects results in the aggregator.
- [struct UITextSearchAggregator](uitextsearchaggregator-swift.struct.md)
  The methods you use on a find session’s aggregator to collect matching text ranges for a search.
- [func compare(UITextRange, toRange: UITextRange, document: Self.DocumentIdentifier?) -> ComparisonResult](uitextsearching-3wkjv/compare(_:torange:document:).md)
  Compares ranges from the set of matches the aggregator provides to determine navigation order.
- [func compare(document: Self.DocumentIdentifier, toDocument: Self.DocumentIdentifier) -> ComparisonResult](uitextsearching-3wkjv/compare(document:todocument:).md)
  Compares documents containing matching ranges from the set the aggregator provides to determine navigation order.
- [associatedtype DocumentIdentifier : Hashable = AnyHashable?](uitextsearching-3wkjv/documentidentifier.md)
  An object that uniquely identifies a specific document when searching for matching text across multiple documents.
### Displaying results
- [func decorate(foundTextRange: UITextRange, document: Self.DocumentIdentifier?, usingStyle: UITextSearchFoundTextStyle)](uitextsearching-3wkjv/decorate(foundtextrange:document:usingstyle:).md)
  Applies the style to a specific text range to indicate found and highlighted results.
- [func clearAllDecoratedFoundText()](uitextsearching-3wkjv/clearalldecoratedfoundtext.md)
  Clears the style from all found and highlighted results.
- [func willHighlight(foundTextRange: UITextRange, document: Self.DocumentIdentifier?)](uitextsearching-3wkjv/willhighlight(foundtextrange:document:).md)
  Informs the searchable object when the highlighted search result is about to change.
- [func scrollRangeToVisible(UITextRange, inDocument: Self.DocumentIdentifier?)](uitextsearching-3wkjv/scrollrangetovisible(_:indocument:).md)
  Scrolls to the containing view to make the text range visible.
### Identifying selected text
- [var selectedTextRange: UITextRange?](uitextsearching-3wkjv/selectedtextrange.md)
  The range of selected text in a document.
- [var selectedTextSearchDocument: Self.DocumentIdentifier?](uitextsearching-3wkjv/selectedtextsearchdocument.md)
  The object that uniquely identifies the specific document with selected text.
### Handling replacements
- [var supportsTextReplacement: Bool](uitextsearching-3wkjv/supportstextreplacement.md)
  A Boolean value that indicates whether the searchable object supports replacing text.
- [func replace(foundTextRange: UITextRange, document: Self.DocumentIdentifier?, withText: String)](uitextsearching-3wkjv/replace(foundtextrange:document:withtext:).md)
  Informs the searchable object to replace the text range for the highlighted search result.
- [func replaceAll(queryString: String, options: UITextSearchOptions, withText: String)](uitextsearching-3wkjv/replaceall(querystring:options:withtext:).md)
  Informs the searchable object to replace all matching text across all searchable documents.
- [func shouldReplace(foundTextRange: UITextRange, document: Self.DocumentIdentifier?, withText: String) -> Bool](uitextsearching-3wkjv/shouldreplace(foundtextrange:document:withtext:).md)
  Determines whether the searchable object allows replacement of the text range you provide.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UITextView](uitextview.md)

## See Also

- [class UIFindInteraction](uifindinteraction.md)
  An interaction that provides text finding and replacing operations using a system find panel.
- [protocol UIFindInteractionDelegate](uifindinteractiondelegate.md)
  A delegate object that provides a session object to manage the search state for a find interaction and receives notifications of search session lifetimes.
- [class UIFindSession](uifindsession.md)
  An abstract base class that manages the state, presentation, and behavior for a search that the find interaction initiates.
- [class UITextSearchingFindSession](uitextsearchingfindsession.md)
  A find session object that wraps a searchable object implementing the text-searching protocol.
- [class UITextSearchOptions](uitextsearchoptions.md)
  An object containing the configurable options for a text search.
- [enum UITextSearchFoundTextStyle](uitextsearchfoundtextstyle.md)
  Constants that describe the style a find session uses to decorate the text.
- [UITextSearchOptions.WordMatchMethod](uitextsearchoptions/wordmatchmethod-swift.enum.md)
  Constants that describe the method to use when searching text for words that match a string.
- [UIFindSession.SearchResultDisplayStyle](uifindsession/searchresultdisplaystyle-swift.enum.md)
  Constants that describe the results summary the find panel UI includes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv)*