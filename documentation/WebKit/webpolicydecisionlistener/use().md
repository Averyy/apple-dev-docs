# use()

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the listener to use the resource.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
func use()
```

```objc
- (void) use;
```

#### Discussion

If there are pending policy decisions, the next policy delegate method has the opportunity to decide what to do with the resource. This will be either the next navigation policy delegate (if there is a redirect), or the content policy delegate. If there are no pending policy decisions, the resource will be displayed if possible. If there is no document view available to display the resource, then the webView:unableToImplementPolicyWithError:frame: message will be sent to the web view policy delegate with an appropriate error. Invoking this method creates any new windows needed to handle the resource.

## See Also

### Related Documentation
- [class func registerClass(AnyClass!, representationClass: AnyClass!, forMIMEType: String!)](../webview-swift.class/registerclass%28_,representationclass,formimetype%29.md)
  Specifies the view and representation objects to be used for specific MIME types.
### Making Resource-Usage Decisions
- [func download()](./download%28%29.md)
  Tells the listener to download the resource instead of displaying it.
- [func ignore()](./ignore%28%29.md)
  Tells the listener to ignore the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpolicydecisionlistener/use())*