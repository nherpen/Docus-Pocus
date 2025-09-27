# Statement of work
## 230180-PDGF: PIC Testing setup

Table: Summary
| Project Name | 230180-PDGF |
|--------------|--------------------------|
| Customer     | Bright Photonics |
| Author       | Noud van Herpen |
| Date         | 14-12-2025|
| Version      | 0.1 |
| Status       | Draft |

## Changelog

Table: Changelog
| Version | Status | Date | Author | Change Summary |
|---------|--------|------|--------|----------------|
| 0.1     | Draft | 13-12-2025 | Noud van Herpen | Initial version |

## Definitions & Abbreviations
PIC Characterisation
P-pi measurement

## Introduction
Bright Photonics aims to ramp up testing of PICs. When a batch of PICs returns from the foundry, only limited performance metrics can be communicated to the customer, due to the high costs (time and financially) of PIC characterisation. PIC characterisation involves yet many manual, laborous steps. By automating these steps, a PIC design can be delivered to the customer, including a statement on Known-Good Die (KGD).

Bright is determined to develop a test setup in their lab that is capable of testing 1000 PICs per day. The setup in mind fulfills functions in three categories:
 1. **Die handling**: Transferring a die from gel-pak to die chuck, positioning the chuck, aligning optical & electrical probes to the PIC & scanning PIC geometry.
 2. **Optical measurements**: Various measurements including a tunable laser, polarisation controller, optical power meter & DC current measurements.
 3. **Overhead**: Data handling & management, sequence generation, safety features, report generation, device management & procedures. 

Ultimately, a gel-pak can be placed in the test setup, PICs will be loaded & unloaded automatically on a chuck where a sequence of optical measurements are executed, resulting in a performance report. Figure N shows this process roughly.

![alt text](../../images/logo_brightphotonics2.png)

PIC designs incorporate numerous microscopic optic devices, each type needing various characterisation measurements. For example, an MZI (Mach-Zehnder Interferometer) would undergo "waveguide loss measurements".

## Services & Deliverables


## Requirements

Table: Requirements
| ID | Requirement | Verification Method |
|----|-------------|---------------------|
| 230180-SOW-01 | The setup can transfer a PIC from gel-pak to chuck with 100 [um] repeatability | Repeatability test|
| 230180-SOW-02 | The setup can process 100 die per hour | Repeatability test|
| | Automatic fiber alignment | |
| | Automatic DC-probe alignment | |
| | Automatic DC-readout | |
| | GUI / HMI | |

## Appendices