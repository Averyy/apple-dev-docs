# SKSummaryCopySentenceSummaryString(_:_:)

**Framework**: Core Services  
**Kind**: func

Gets a text string consisting of a summary with, at most, the requested number of sentences.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SKSummaryCopySentenceSummaryString(_ summary: SKSummary!, _ numSentences: CFIndex) -> Unmanaged<CFString>!
```

#### Return_value

A [`CFString`](https://developer.apple.com/documentation/corefoundation/cfstring) object containing the requested summary.

## Parameters

- `summary`: The summarization object containing the text from which you want a summarization.
- `numSentences`: The maximum number of sentences you want in the summary.

## See Also

- [func SKSummaryCreateWithString(CFString!) -> Unmanaged<SKSummary>!](1446229-sksummarycreatewithstring.md)
  Creates a summary object based on a text string.
- [func SKSummaryGetSentenceSummaryInfo(SKSummary!, CFIndex, UnsafeMutablePointer<CFIndex>!, UnsafeMutablePointer<CFIndex>!, UnsafeMutablePointer<CFIndex>!) -> CFIndex](1444767-sksummarygetsentencesummaryinfo.md)
  Gets detailed information about a body of text for constructing a custom sentence-based summary string.
- [func SKSummaryGetParagraphSummaryInfo(SKSummary!, CFIndex, UnsafeMutablePointer<CFIndex>!, UnsafeMutablePointer<CFIndex>!) -> CFIndex](1447517-sksummarygetparagraphsummaryinfo.md)
  Gets detailed information about a body of text for constructing a custom paragraph-based summary string.
- [func SKSummaryGetSentenceCount(SKSummary!) -> CFIndex](1450009-sksummarygetsentencecount.md)
  Gets the number of sentences in a summarization object.
- [func SKSummaryGetParagraphCount(SKSummary!) -> CFIndex](1449304-sksummarygetparagraphcount.md)
  Gets the number of paragraphs in a summarization object.
- [func SKSummaryCopySentenceAtIndex(SKSummary!, CFIndex) -> Unmanaged<CFString>!](1450287-sksummarycopysentenceatindex.md)
  Gets a specified sentence from the text in a summarization object.
- [func SKSummaryCopyParagraphAtIndex(SKSummary!, CFIndex) -> Unmanaged<CFString>!](1445711-sksummarycopyparagraphatindex.md)
  Gets a specified paragraph from the text in a summarization object.
- [func SKSummaryCopyParagraphSummaryString(SKSummary!, CFIndex) -> Unmanaged<CFString>!](1449746-sksummarycopyparagraphsummarystr.md)
  Gets a text string consisting of a summary with, at most, the requested number of paragraphs.
- [func SKSummaryGetTypeID() -> CFTypeID](1444796-sksummarygettypeid.md)
  Gets the type identifier for Search Kit summarization objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1449700-sksummarycopysentencesummarystri)*