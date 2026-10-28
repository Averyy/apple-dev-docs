# UITextSearching

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

The methods you use on a find session’s searchable objects to perform search operations and decorate the found text results.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```objc
@protocol UITextSearching <NSObject>
```

## Overview

Implement this protocol on the class that encapsulates the searchable content for your view. This allows you to use an instance of [`UITextSearchingFindSession`](./uitextsearchingfindsession.md) to manage the session for a find interaction.

## Topics

### Handling searches
- [- performTextSearchWithQueryString:usingOptions:resultAggregator:](./uitextsearching-53wjq/performtextsearchwithquerystring_usingoptions_resultaggregator_.md)
  Searches for ranges of text matching the string across all searchable documents and collects results in the aggregator.
- [UITextSearchAggregator](./uitextsearchaggregator-c.protocol.md)
  The methods you use on a find session’s aggregator to collect matching text ranges for a search.
- [- compareFoundRange:toRange:inDocument:](./uitextsearching-53wjq/comparefoundrange_torange_indocument_.md)
  Compares ranges from the set of matches the aggregator provides to determine navigation order.
- [- compareOrderFromDocument:toDocument:](./uitextsearching-53wjq/compareorderfromdocument_todocument_.md)
  Compares documents containing matching ranges from the set the aggregator provides to determine navigation order.
- [UITextSearchDocumentIdentifier](./uitextsearchdocumentidentifier.md)
  A string that uniquely identifies a specific document when searching for matching text across multiple documents.
### Displaying results
- [- decorateFoundTextRange:inDocument:usingStyle:](./uitextsearching-53wjq/decoratefoundtextrange_indocument_usingstyle_.md)
  Applies the style to a specific text range to indicate found and highlighted results.
- [- clearAllDecoratedFoundText](./uitextsearching-53wjq/clearalldecoratedfoundtext.md)
  Clears the style from all found and highlighted results.
- [- willHighlightFoundTextRange:inDocument:](./uitextsearching-53wjq/willhighlightfoundtextrange_indocument_.md)
  Informs the searchable object when the highlighted search result is about to change.
- [- scrollRangeToVisible:inDocument:](./uitextsearching-53wjq/scrollrangetovisible_indocument_.md)
  Scrolls to the containing view to make the text range visible.
### Identifying selected text
- [selectedTextRange](./uitextsearching-53wjq/selectedtextrange.md)
  The range of selected text in a document.
- [selectedTextSearchDocument](./uitextsearching-53wjq/selectedtextsearchdocument.md)
  The object that uniquely identifies the specific document with selected text.
### Handling replacements
- [supportsTextReplacement](./uitextsearching-53wjq/supportstextreplacement.md)
  A Boolean value that indicates whether the searchable object supports replacing text.
- [- replaceFoundTextInRange:inDocument:withText:](./uitextsearching-53wjq/replacefoundtextinrange_indocument_withtext_.md)
  Informs the searchable object to replace the text range for the highlighted search result.
- [- replaceAllOccurrencesOfQueryString:usingOptions:withText:](./uitextsearching-53wjq/replacealloccurrencesofquerystring_usingoptions_withtext_.md)
  Informs the searchable object to replace all matching text across all searchable documents.
- [- shouldReplaceFoundTextInRange:inDocument:withText:](./uitextsearching-53wjq/shouldreplacefoundtextinrange_indocument_withtext_.md)
  Determines whether the searchable object allows replacement of the text range you provide.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [UITextView](./uitextview.md)

## See Also

### Find and replace
- [class UIFindInteraction](./uifindinteraction.md)
  An interaction that provides text finding and replacing operations using a system find panel.
- [protocol UIFindInteractionDelegate](./uifindinteractiondelegate.md)
  A delegate object that provides a session object to manage the search state for a find interaction and receives notifications of search session lifetimes.
- [class UIFindSession](./uifindsession.md)
  An abstract base class that manages the state, presentation, and behavior for a search that the find interaction initiates.
- [class UITextSearchingFindSession](./uitextsearchingfindsession.md)
  A find session object that wraps a searchable object implementing the text-searching protocol.
- [class UITextSearchOptions](./uitextsearchoptions.md)
  An object containing the configurable options for a text search.
- [enum UITextSearchFoundTextStyle](./uitextsearchfoundtextstyle.md)
  Constants that describe the style a find session uses to decorate the text.
- [UITextSearchOptions.WordMatchMethod](./uitextsearchoptions/wordmatchmethod-swift.enum.md)
  Constants that describe the method to use when searching text for words that match a string.
- [UIFindSession.SearchResultDisplayStyle](./uifindsession/searchresultdisplaystyle-swift.enum.md)
  Constants that describe the results summary the find panel UI includes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-53wjq)*