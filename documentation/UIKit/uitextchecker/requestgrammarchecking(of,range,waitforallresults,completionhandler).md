# requestGrammarChecking(of:range:waitForAllResults:completionHandler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func requestGrammarChecking(of stringToCheck: String, range: NSRange, waitForAllResults: Bool, completionHandler: (([NSTextCheckingResult]) -> Void)? = nil)
```

```swift
func requestGrammarChecking(of stringToCheck: String, range: NSRange, waitForAllResults: Bool) async -> [NSTextCheckingResult]
```

```objc
- (void) requestGrammarCheckingOfString:(NSString *) stringToCheck range:(NSRange) range waitForAllResults:(BOOL) waitForAllResults completionHandler:(void (^)(NSArray<NSTextCheckingResult *> *results)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextchecker/requestgrammarchecking(of:range:waitforallresults:completionhandler:))*