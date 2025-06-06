# perform(_:)

**Framework**: Vision  
**Kind**: method

Schedules Vision requests to perform.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func perform(_ requests: [VNRequest]) throws
```

#### Discussion

The function returns after all requests have either completed or failed. Check individual requests and errors for their respective successes and failures.

## Parameters

- `requests`: An array of Vision requests to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnimagerequesthandler/perform(_:))*