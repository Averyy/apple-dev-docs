# webView(_:insertInputSuggestion:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
optional func webView(_ webView: WKWebView, insertInputSuggestion inputSuggestion: UIInputSuggestion)
```

```objc
- (void) webView:(WKWebView *) webView insertInputSuggestion:(UIInputSuggestion *) inputSuggestion;
```

#### Discussion

Tells the delegate when the keyboard delivers an input suggestion.

## Parameters

- `webView`: The web view where the input suggestion should be inserted.
- `inputSuggestion`: The input suggestion that the user or system selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webview(_:insertinputsuggestion:))*