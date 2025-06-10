# init(options:)

**Framework**: Core Image  
**Kind**: init

Initializes a context without a specific rendering destination, using the specified options.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
init(options: [CIContextOption : Any]? = nil)
```

#### Return Value

An initialized Core Image context.

#### Discussion

If you create a context without specifying a rendering destination, Core Image automatically chooses and internally manages a rendering destination based on the current device’s capabilities and your settings in the `options` dictionary. You cannot use a context without an explicit destination for the methods listed in Drawing Images. Instead, use the methods listed in Rendering Images.

The `options` dictionary defines behaviors for the context, such as color space and rendering quality. For example, to create a CPU-based context, use the  [`useSoftwareRenderer`](cicontextoption/usesoftwarerenderer.md) key.

## Parameters

- `options`: A dictionary containing options for the context. For applicable keys and values, see  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/init(options:))*