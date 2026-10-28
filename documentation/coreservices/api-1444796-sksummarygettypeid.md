# SKSummaryGetTypeID()

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Gets the type identifier for Search Kit summarization objects.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SKSummaryGetTypeID() -> CFTypeID
```

```c
CFTypeID SKSummaryGetTypeID(void);
```

## Return Value

A CFTypeID object, or `NULL` on failure.

## Discussion

Search Kit represents summarization results with summarization objects ([`SKSummary`](./sksummary.md) opaque types). If your code needs to determine whether a particular data type is a summary, you can use this function along with the [`CFGetTypeID(_:)`](../CoreFoundation/cfgettypeid%28_%29.md) function and perform a comparison.

Never hard-code the summarization type ID because it can change from one release of macOS to another.

## See Also

### Working With Summarization
- [func SKSummaryCreateWithString(CFString!) -> Unmanaged<SKSummary>!](./api-1446229-sksummarycreatewithstring.md)
  Creates a summary object based on a text string.
- [func SKSummaryGetSentenceSummaryInfo(SKSummary!, CFIndex, UnsafeMutablePointer<CFIndex>!, UnsafeMutablePointer<CFIndex>!, UnsafeMutablePointer<CFIndex>!) -> CFIndex](./api-1444767-sksummarygetsentencesummaryinfo.md)
  Gets detailed information about a body of text for constructing a custom sentence-based summary string.
- [func SKSummaryGetParagraphSummaryInfo(SKSummary!, CFIndex, UnsafeMutablePointer<CFIndex>!, UnsafeMutablePointer<CFIndex>!) -> CFIndex](./api-1447517-sksummarygetparagraphsummaryinfo.md)
  Gets detailed information about a body of text for constructing a custom paragraph-based summary string.
- [func SKSummaryGetSentenceCount(SKSummary!) -> CFIndex](./api-1450009-sksummarygetsentencecount.md)
  Gets the number of sentences in a summarization object.
- [func SKSummaryGetParagraphCount(SKSummary!) -> CFIndex](./api-1449304-sksummarygetparagraphcount.md)
  Gets the number of paragraphs in a summarization object.
- [func SKSummaryCopySentenceAtIndex(SKSummary!, CFIndex) -> Unmanaged<CFString>!](./api-1450287-sksummarycopysentenceatindex.md)
  Gets a specified sentence from the text in a summarization object.
- [func SKSummaryCopyParagraphAtIndex(SKSummary!, CFIndex) -> Unmanaged<CFString>!](./api-1445711-sksummarycopyparagraphatindex.md)
  Gets a specified paragraph from the text in a summarization object.
- [func SKSummaryCopySentenceSummaryString(SKSummary!, CFIndex) -> Unmanaged<CFString>!](./api-1449700-sksummarycopysentencesummarystri.md)
  Gets a text string consisting of a summary with, at most, the requested number of sentences.
- [func SKSummaryCopyParagraphSummaryString(SKSummary!, CFIndex) -> Unmanaged<CFString>!](./api-1449746-sksummarycopyparagraphsummarystr.md)
  Gets a text string consisting of a summary with, at most, the requested number of paragraphs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444796-sksummarygettypeid)*