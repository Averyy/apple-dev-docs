# supportedJointNamesAndReturnError:

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Retrieves the joint names the request supports.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
- (NSArray<NSString *> *) supportedJointNamesAndReturnError:(NSError **) error;
```

## Return Value

The array of joint names.

## Parameters

- `error`: If an error occurs, an object that describes the error; otherwise, `nil`.

## See Also

### Determining Supported Joints
- [- supportedJointsGroupNamesAndReturnError:](./supportedjointsgroupnamesandreturnerror_.md)
  Retrieves the joint group names the request supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectanimalbodyposerequest/supportedjointnamesandreturnerror:)*