# init(cgContext:options:)

**Framework**: Core Image  
**Kind**: init

Creates a Core Image context from a Quartz context, using the specified options.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(cgContext cgctx: CGContext, options: [CIContextOption : Any]? = nil)
```

#### Discussion

After calling this method, Core Image draws content to the specified Quartz graphics context.

When you create a [`CIContext`](cicontext.md) object using a Quartz graphics context, any transformations that are already set on the Quartz graphics context affect drawing to that context.

> **Note**:  To obtain a Core Image context for the current AppKit drawing context in macOS, use the [`NSGraphicsContext`](https://developer.apple.com/documentation/AppKit/NSGraphicsContext) [`ciContext`](https://developer.apple.com/documentation/AppKit/NSGraphicsContext/ciContext) property.

## Parameters

- `cgctx`: A Quartz graphics context (  object) either obtained from the system or created using a Quartz function such as  doc://com.apple.documentation/documentation/coregraphics/cgcontext/1455939-init . See   for information on creating Quartz graphics contexts.
- `options`: A dictionary that contains color space information. You can pass any of the keys defined in   along with the appropriate value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/init(cgcontext:options:))*