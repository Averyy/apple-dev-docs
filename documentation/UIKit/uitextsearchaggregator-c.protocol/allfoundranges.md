# allFoundRanges

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An ordered set of all the text ranges that match the search.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, readonly) NSOrderedSet<UITextRange *> * allFoundRanges;
```

## See Also

### Tracking search results
- [- foundRange:forSearchString:inDocument:](./foundrange_forsearchstring_indocument_.md)
  Adds a text range to the set of matches.
- [- invalidateFoundRange:inDocument:](./invalidatefoundrange_indocument_.md)
  Removes a text range from the set of matches.
- [- invalidate](./invalidate.md)
  Invalidates all currently shown ranges.
- [- finishedSearching](./finishedsearching.md)
  Finishes the search for text ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearchaggregator-c.protocol/allfoundranges)*