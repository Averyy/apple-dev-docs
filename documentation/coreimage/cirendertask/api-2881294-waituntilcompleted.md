# waitUntilCompleted()

**Framework**: Core Image  
**Kind**: instm

Waits until the [`CIRenderTask`](cirendertask.md) finishes and returns.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func waitUntilCompleted() throws -> CIRenderInfo
```

#### Discussion

Synchronously blocks execution until the [`CIRenderTask`](cirendertask.md) either completes or fails (with error).  Calling this method after [`startTask(toRender:to:)`](cicontext/2875429-starttask.md) or [`startTask(toRender:from:to:at:)`](cicontext/2875448-starttask.md) makes the render task behave synchronously, as if the CPU and GPU were operating as a single unit.

## Parameters

- `error`: nil unless the render task failed


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirendertask/2881294-waituntilcompleted)*