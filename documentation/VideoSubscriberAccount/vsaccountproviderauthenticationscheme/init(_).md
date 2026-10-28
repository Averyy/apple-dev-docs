# init(_:)

**Framework**: Video Subscriber Account  
**Kind**: init  
**Role**: Initializer

Creates a new authentication scheme with the specified string.

**Availability**:
- iOS
- iPadOS
- macOS
- tvOS
- visionOS

## Declaration

```swift
init(_ rawValue: String)
```

## Discussion

This initializer returns `nil` if the string value you specify doesn’t correspond to a valid authentication scheme type.

## Parameters

- `rawValue`: The string to use to create the authentication scheme.

## See Also

### Creating an Authentication Scheme
- [init(rawValue: String)](./init%28rawvalue%29.md)
  Creates a new authentication scheme with the specified raw value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountproviderauthenticationscheme/init(_:))*