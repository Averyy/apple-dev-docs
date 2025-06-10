# URLSchemeTaskResult.data(_:)

**Framework**: WebKit  
**Kind**: case

Data for the resource. This value may contain all of the data or only some of it.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
case data(Data)
```

#### Discussion

If you load the data incrementally, multiple of these values may be added to the result sequence to deliver each new portion of data. Each time some new Data is added to the sequence, WebKit appends the data to any previously received data.

A [`URLSchemeTaskResult.response(_:)`](urlschemetaskresult/response(_:).md) must have been added to the sequence prior to any data being aded to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/urlschemetaskresult/data(_:))*