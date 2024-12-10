# Spy device: playback of sound in the room by HDD vibration

## Authors
- (Maksym Buleshnyi)[https://github.com/maksDev123]
- (Mykhailo Buleshnyi)[https://github.com/mikl123]
- (Artur Pelcharskyi)[https://github.com/PelArtur]
- (Yuliia Moliashcha)[https://github.com/bulkobubulko]

## Project Overview

Hard disk drives (HDDs), while not originally designed to function as acoustic sensors, possess internal components inherently sensitive to vibrations, including those induced by sound waves. These vibrations result in displacements of the HDD head, i.e., Position Error Signal (PES) measurements, suggesting that PES can serve as a proxy for detecting external sound waves.

This project aims to investigate the influence of sound waves on HDDs and explore methodologies for measuring PES to analyze acoustic waves, analogous to the functionality of a microphone.

## Approaches
1. SMART status
2. kscope
3. PES

## Impact of sound on PES

PES in calm condition:

![pes-silent](/data/pes-silent.png)

PES under influence of sound:

![pes-sound](/data/pes-sound.png)

## Results 

[Paper](https://www.overleaf.com/project/670cf78c14e80a299384173c)

[Presentation](https://docs.google.com/presentation/d/1J7DsvozCx6ya57X8JyggiJmysw4fNvPFUtXx2ukg5J8/edit?usp=sharing)

[Demonstration](https://www.youtube.com/watch?v=RUG950oKycg)