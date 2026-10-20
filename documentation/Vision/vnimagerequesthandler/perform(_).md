# perform(_:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) performRequests:(NSArray<VNRequest *> *) requests error:(NSError **) error;
```

#### Discussion

The function returns after all requests have either completed or failed. Check individual requests and errors for their respective successes and failures.

## Parameters

- `requests`: An array of Vision requests to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnimagerequesthandler/perform(_:))*