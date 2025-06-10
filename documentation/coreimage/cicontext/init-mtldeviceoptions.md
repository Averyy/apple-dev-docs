# init(mtlDevice:options:)

**Framework**: Core Image  
**Kind**: init

Creates a Core Image context using the specified Metal device and options.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(mtlDevice device: any MTLDevice, options: [CIContextOption : Any]? = nil)
```

#### Return Value

A Core Image context.

#### Discussion

Use this method to choose a specific Metal device for rendering when a system contains multiple Metal devices. To create a Metal-based context using the system’s default Metal device, use the [`contextWithOptions:`](cicontext/contextwithoptions:.md) method.

## Parameters

- `device`: The Metal device object to use for rendering.
- `options`: A dictionary that contains options for creating a   object. You can pass any of the keys defined in   along with the appropriate value.

## See Also

- [init(mtlDevice: any MTLDevice)](cicontext/init(mtldevice:).md)
  Creates a Core Image context using the specified Metal device.
- [init(mtlCommandQueue: any MTLCommandQueue)](cicontext/init(mtlcommandqueue:).md)
- [init(mtlCommandQueue: any MTLCommandQueue, options: [CIContextOption : Any]?)](cicontext/init(mtlcommandqueue:options:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/init(mtldevice:options:))*