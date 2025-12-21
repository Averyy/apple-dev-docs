# URLSchemeTaskResult.data(_:)

**Framework**: WebKit  
**Kind**: case

Data for the resource. This value may contain all of the data or only some of it.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case data(Data)
```

#### Discussion

If you load the data incrementally, multiple of these values may be added to the result sequence to deliver each new portion of data. Each time some new Data is added to the sequence, WebKit appends the data to any previously received data.

A [`URLSchemeTaskResult.response(_:)`](urlschemetaskresult/response(_:).md) must have been added to the sequence prior to any data being aded to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/urlschemetaskresult/data(_:))*