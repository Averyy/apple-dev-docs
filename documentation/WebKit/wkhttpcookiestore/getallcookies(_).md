# getAllCookies(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Fetches all stored cookies asynchronously and delivers them to the specified completion handler.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
func getAllCookies(_ completionHandler: @escaping @MainActor @Sendable ([HTTPCookie]) -> Void)
```

```swift
func allCookies() async -> [HTTPCookie]
```

```objc
- (void) getAllCookies:(void (^)(NSArray<NSHTTPCookie *> *)) completionHandler;
```

#### Discussion

Use this method to get the set of cookies currently associated with your web view. Iterate over the contents of the provided array to retrieve the specific cookie you need for your code.

## Parameters

- `completionHandler`: A completion handler block to execute asynchronously with the results. This block has no return value and takes the following parameter:

  - **cookieArray**: An array of [`HTTPCookie`](../../Foundation/httpcookie.md) objects. If the store contains no cookies, this parameter contains an empty array.

## See Also

### Managing cookies
- [func setCookie(HTTPCookie, completionHandler: (() -> Void)?)](./setcookie%28_,completionhandler%29.md)
  Adds a cookie to the cookie store.
- [func delete(HTTPCookie, completionHandler: (() -> Void)?)](./delete%28_,completionhandler%29.md)
  Deletes the specified cookie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkhttpcookiestore/getallcookies(_:))*