# SKSummaryGetSentenceSummaryInfo(_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Gets detailed information about a body of text for constructing a custom sentence-based summary string.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SKSummaryGetSentenceSummaryInfo(_ summary: SKSummary!, _ numSentencesInSummary: CFIndex, _ outRankOrderOfSentences: UnsafeMutablePointer<CFIndex>!, _ outSentenceIndexOfSentences: UnsafeMutablePointer<CFIndex>!, _ outParagraphIndexOfSentences: UnsafeMutablePointer<CFIndex>!) -> CFIndex
```

#### Return_value

The number of sentences in the summary.

## Parameters

- `summary`: The summarization object containing the text from which you want to build a summary.
- `numSentencesInSummary`: The maximum number of sentences you want in the summary.
- `outRankOrderOfSentences`: On input, a pointer to an array of CFIndex objects. On output, points to the previously allocated array, which now lists the summarization relevance rank of each sentence in the original text. The most important sentence gets a rank of 1. The array size must equal  , or else be   if you don’t want to get the rank orders.
- `outSentenceIndexOfSentences`: On input, a pointer to an array of CFIndex objects. On output, points to the previously allocated array, which now contains the ordinal number for each sentence in the original text. Use the   function with one of these numbers to get the corresponding sentence. The array size must equal  , or else be   if you don’t want to get the ordinal numbers of the sentences.
- `outParagraphIndexOfSentences`: On input, a pointer to an array of CFIndex objects. On output, points to the previously allocated array, which now contains the ordinal number for the paragraph that each corresponding sentence, referenced in  , appears in. The array size must equal  , or else be   if you don’t want to get the ordinal numbers of the sentences.

## See Also

- [func SKSummaryCreateWithString(CFString!) -> Unmanaged<SKSummary>!](1446229-sksummarycreatewithstring.md)
  Creates a summary object based on a text string.
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
- [func SKSummaryCopySentenceSummaryString(SKSummary!, CFIndex) -> Unmanaged<CFString>!](1449700-sksummarycopysentencesummarystri.md)
  Gets a text string consisting of a summary with, at most, the requested number of sentences.
- [func SKSummaryCopyParagraphSummaryString(SKSummary!, CFIndex) -> Unmanaged<CFString>!](1449746-sksummarycopyparagraphsummarystr.md)
  Gets a text string consisting of a summary with, at most, the requested number of paragraphs.
- [func SKSummaryGetTypeID() -> CFTypeID](1444796-sksummarygettypeid.md)
  Gets the type identifier for Search Kit summarization objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444767-sksummarygetsentencesummaryinfo)*