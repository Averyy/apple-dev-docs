# CoreEndianFlipProc

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Defines a pointer to a callback function thatbyte-swaps your custom data.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.4+

## Declaration

```c
typedef OSStatus (*CoreEndianFlipProc)(OSType dataDomain, OSType dataType, SInt16 id, void *dataPtr, ByteCount dataSize, Boolean currentlyNative, void *refcon);
```

#### Return Value

A result code thatindicates whether the byte swapping is successful. Your callbackshould return `noErr` ifthe resource is byte swapped without error, `handlerNotFound` ifyou chose not to byte swap the data, and the appropriate resultcode to indicate an error condition if the data is bad. The resultcode you return is propagated through the appropriate manager (ResourceManager (`ResError`) orApple Event Manager) to the caller. 

#### Discussion

You would declare your flipper callback function as followsif your were to name it `MyCoreEndianFlipProc`:

##### Discussion

You should write each flipper callback so it traverses thedata structure that contains the data and performs the followingtasks: 

- Byte swaps all Resource Manager counts and lengthsso that array indexes are associated with the appropriate value
- Byte swaps all integers and longs so that when you read theminto variables of a compatible type the values can be operated oncorrectly (such as numerical, offset, and shift operations) 

A flipper callback must be bidirectional because it can becalled by the Resource Manager or Apple Event Manager when you readdata as well as when you write data. The system ensures that yourflipper callback is invoked at the appropriate times. 

Your flipper callback is not invoked on a microprocessor thatuses big-endian byte ordering. It is called with `currentlyNative` setto `false` when data isread (or received) and `true` whenthe data is set to be written (or sent).

## Parameters

- `dataDomain`: An `OSType` value that specifies the domain to which the flipper callback applies. The value `kCoreEndianResourceManagerDomain`	signifies the domain is resource data. The value `kCoreEndianAppleEventManagerDomain` signifies the domain is Apple event data. See [Domain Types](./api-1575588-domain_types.md) for more information on the values that can be passed to your callback.
- `dataType`: The type of data to be byte swapped by the callback. This is the four character code of the resource type or Apple event.
- `id`: The resource id of the data type. The value `0` signifies the data is not a resource.
- `dataPtr`: On input, points to the data to be flipped. On output, points to the byte-swapped data.
- `dataSize`: The size of the data pointed to the by the `dataPtr` parameter.
- `currentlyNative`: A Boolean value that indicates the direction to byte swap. The value `true` specifies the data pointed to by the `dataPtr` parameter uses the byte ordering of the currently executing code. On a PowerPC system, `true` specifies that the data is in big-endian format. On an x86 system, `true` specifies that the data is in little-endian format.
- `refcon`: A 32-bit value that contains or refers to data needed by the callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/coreendianflipproc)*