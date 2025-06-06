# SKSummaryGetParagraphSummaryInfo(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Gets detailed information about a body of text for constructing a custom paragraph-based summary string.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SKSummaryGetParagraphSummaryInfo(_ summary: SKSummary!, _ numParagraphsInSummary: CFIndex, _ outRankOrderOfParagraphs: UnsafeMutablePointer<CFIndex>!, _ outParagraphIndexOfParagraphs: UnsafeMutablePointer<CFIndex>!) -> CFIndex
```

#### Return_value

The number of paragraphs in the summary.

## Parameters

- `summary`: The summarization object containing the text from which you want to build a summary.
- `numParagraphsInSummary`: The maximum number of paragraphs you want in the summary.
- `outRankOrderOfParagraphs`: On input, a pointer to an array of CFIndex objects. On output, points to the previously allocated array, which now lists the summarization relevance rank of each paragraph in the original text. The most important paragraph gets a rank of 1. The array size must equal  , or else be   if you don’t want to get the relevance ranks.
- `outParagraphIndexOfParagraphs`: On output, points to an array containing the ordinal number for each paragraph in the original text. Use the   function with one of these numbers to get the corresponding paragraph. The array size must equal  , or else be   if you don’t want to get the ordinal numbers of the paragraphs.

## See Also

- [func SKSummaryCreateWithString(CFString!) -> Unmanaged<SKSummary>!](1446229-sksummarycreatewithstring.md)
  Creates a summary object based on a text string.
- [func SKSummaryGetSentenceSummaryInfo(SKSummary!, CFIndex, UnsafeMutablePointer<CFIndex>!, UnsafeMutablePointer<CFIndex>!, UnsafeMutablePointer<CFIndex>!) -> CFIndex](1444767-sksummarygetsentencesummaryinfo.md)
  Gets detailed information about a body of text for constructing a custom sentence-based summary string.
- [func SKSummaryGetSentenceCount(SKSummary!) -> CFIndex](1450009-sksummarygetsentencecount.md)
  Gets the number of sentences in a summarization object.
- [func SKSummaryGetParagraphCount(SKSummary!) -> CFIndex](1449304-sksummarygetparagraphcount.md)
  Gets the number of paragraphs in a summarization object.
- [func SKSummaryCopySentenceAtIndex(SKSummary!, CFIndex) -> Unmanaged<CFString>!](1450287-sksummarycopysentenceatindex.md)
  Gets a specified sentence from the text in a summarization object.
- [func SKSummaryCopyParagraphAtIndex(SKSummary!, CFIndex) -> Unmanaged<CFString>!](1445711-sksummarycopyparagraphatindex.md)
  Gets a specified paragraph from the text in a summarization object.
- [func SKSummaryCopySentenceSummaryString(SKSummary!, CFIndex) -> Unmanaged<CFString>!](1449700-sksummarycopysentencesummarystri.md)
  Gets a text string consisting of a summary with, at most, the requested number of sentences.
- [func SKSummaryCopyParagraphSummaryString(SKSummary!, CFIndex) -> Unmanaged<CFString>!](1449746-sksummarycopyparagraphsummarystr.md)
  Gets a text string consisting of a summary with, at most, the requested number of paragraphs.
- [func SKSummaryGetTypeID() -> CFTypeID](1444796-sksummarygettypeid.md)
  Gets the type identifier for Search Kit summarization objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447517-sksummarygetparagraphsummaryinfo)*