# initWithName:error:

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Initialize options to set on a Rosetta directory share.

**Availability**:
- macOS 14.0+

## Declaration

```objc
- (instancetype) initWithName:(NSString *) name error:(NSError **) error;
```

## Discussion

The `sockaddr_un` structure in Linux defines the maximum allowed length of `name`.

## Parameters

- `name`: This is the name of the abstract socket that Rosetta uses.
- `error`: If not `nil`, assigned with the error if the initialization fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzlinuxrosettaabstractsocketcachingoptions/initwithname:error:)*