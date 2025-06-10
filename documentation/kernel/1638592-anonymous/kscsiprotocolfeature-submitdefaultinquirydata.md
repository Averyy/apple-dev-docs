# kSCSIProtocolFeature_SubmitDefaultInquiryData

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.12+

## Declaration

```swift
kSCSIProtocolFeature_SubmitDefaultInquiryData = 10
```

#### Discussion

If the SCSI Protocol Services Driver needs any extra information to make any negotiation settings from the standard INQUIRY data, this will be called to set that appropriately. The serviceValue will point to a SCSICmd_INQUIRY_StandardData buffer. The size of the buffer depends on the SCSI Device Characteristics dictionary for the device or bus. If there is no kIOPropertySCSIInquiryLengthKey value set in the dictionary or if it doesn't exist, then the size of the data will be the size of the full amount of Inquiry retrieved from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1638592-anonymous/kscsiprotocolfeature_submitdefaultinquirydata)*