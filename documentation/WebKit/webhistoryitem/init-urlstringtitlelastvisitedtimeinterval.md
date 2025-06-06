# init(urlString:title:lastVisitedTimeInterval:)

**Framework**: Webkit  
**Kind**: init

Initializes the receiver with a URL,`URLString`, a title specified by `title` and the last time this item was visited specified by `time` title, and time last visited.

**Availability**:
- macOS 10.3+

## Declaration

```swift
init!(urlString URLString: String!, title: String!, lastVisitedTimeInterval time: TimeInterval)
```

#### Discussion

WebKit normally creates WebHistoryItem objects for you but on occasion you might want to create an item and add it to the WebBackForwardList yourself. Note that when an instance is first initialized the strings returned by [`urlString`](webhistoryitem/urlstring.md) and [`originalURLString`](webhistoryitem/originalurlstring.md) are the same.

## See Also

- [WebKit Objective-C Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistoryitem/init(urlstring:title:lastvisitedtimeinterval:))*