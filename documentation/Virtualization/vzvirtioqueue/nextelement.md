# nextElement()

**Framework**: Virtualization  
**Kind**: method

Gets the next element in this queue, if any.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func nextElement() -> VZVirtioQueueElement?
```

#### Return Value

The next available element on this queue, or `nil` if no elements are available or if the device is no longer live.

#### Discussion

Use this method to obtain any elements (available buffers), that the Virtualization framework represents as `VZVirtioQueueElement`, in the virtqueue for processing.

You need to call the [`returnToQueue()`](vzvirtioqueueelement/returntoqueue().md) method when you are finished processing the element in order to return the element back to the guest.

When using this method, the framework disables virtqueue notifications until you have consumed every available element. When calling this method in response to a virtqueue notification, you need to do so repeatedly until it returns `nil` (which indicates there are no more elements available in the queue), typically in a loop like this:

**Objective-C**:

```objc
    VZVirtioQueue *queue = ...
    while (VZVirtioQueueElement *element = [queue nextElement]) {
        // Code to process the element.
    }
```

**Swift**:

```swift
    let queue: VZVirtioQueue = ...
    while let element = queue.nextElement() {
        // Code to process the element.
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioqueue/nextelement())*