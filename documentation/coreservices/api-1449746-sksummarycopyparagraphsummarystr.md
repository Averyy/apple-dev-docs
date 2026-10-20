# SKSummaryCopyParagraphSummaryString(_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Gets a text string consisting of a summary with, at most, the requested number of paragraphs.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SKSummaryCopyParagraphSummaryString(_ summary: SKSummary!, _ numParagraphs: CFIndex) -> Unmanaged<CFString>!
```

```c
CFStringRef SKSummaryCopyParagraphSummaryString(SKSummaryRef summary, CFIndex numParagraphs);
```

#### Return Value

A [`CFString`](../CoreFoundation/cfstring.md) object containing the requested summary.

## Parameters

- `summary`: The summarization object containing the text from which you want a summarization.
- `numParagraphs`: The maximum number of paragraphs you want in the summary.

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
- [func SKSummaryGetTypeID() -> CFTypeID](./api-1444796-sksummarygettypeid.md)
  Gets the type identifier for Search Kit summarization objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1449746-sksummarycopyparagraphsummarystr)*