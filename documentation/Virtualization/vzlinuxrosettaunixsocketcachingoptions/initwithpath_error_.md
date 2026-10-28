# initWithPath:error:

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Creates a new Rosetta caching options object for a UNIX domain socket with the path you specify.

**Availability**:
- macOS 14.0+

## Declaration

```objc
- (instancetype) initWithPath:(NSString *) path error:(NSError **) error;
```

## Discussion

You can optionally configure Rosetta to use cached translations from the Rosetta translation daemon communicating through a UNIX domain socket.

If `path` length exceeds [`maximumPathLength`](./maximumpathlength.md) in UTF-8 bytes, the framework returns `nil` and sets the `error` value, if available.

> ❗ **Important**:  The guest operating system needs to have a directory at `path` created in order for translation caching to operate correctly.

## Parameters

- `path`: The path of the UNIX Domain Socket that Rosetta uses.
- `error`: If not `nil`, assigned with the error if the initialization fails.

## See Also

### Initializers
- [- init](./init.md)
  Creates a new Rosetta caching options object for a UNIX domain socket.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzlinuxrosettaunixsocketcachingoptions/initwithpath:error:)*