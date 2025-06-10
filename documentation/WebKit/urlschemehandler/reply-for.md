# reply(for:)

**Framework**: WebKit  
**Kind**: method  
**Required**: Yes

Produces a sequence of intermixed responses and data to load a resource for a given request.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
func reply(for request: URLRequest) -> Self.TaskSequence
```

#### Discussion

Upon receiving the request, determine the size of the resource and add a [`URLSchemeTaskResult.response(_:)`](urlschemetaskresult/response(_:).md) value to the async sequence. Providing a response mirrors the behavior that a web server performs when it receives a request.

After you load some portion of the resource data, add a [`URLSchemeTaskResult.data(_:)`](urlschemetaskresult/data(_:).md) value to the sequence. Multiple of these values may be added to the sequence to delivery data incrementally, or a single one with all of the data.

If an error occurs at any point during the load process, a value of type `Failure` can be thrown to report it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/urlschemehandler/reply(for:))*