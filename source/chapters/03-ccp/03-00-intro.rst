CCP刻蚀系统深度解析
===========

.. mermaid::

   graph TB
       subgraph CCP刻蚀系统完整架构
           subgraph 顶部区域
               SH[Showerhead喷淋头<br/>材料: Si/SiC/Al<br/>功能: 气体分配]
               UE[上电极<br/>材料: Si/SiC/Al<br/>功能: 等离子体激发<br/>通常接地]
               GA[气体分配盘<br/>材料: SiC/石英<br/>功能: 均匀混气]
           end

           subgraph 等离子体区域
               P[等离子体区域<br/>密度: 10⁹-10¹⁰ cm⁻³<br/>电子温度: 3-8 eV<br/>工作气压: 10-500 mTorr]
           end

           subgraph 底部区域
               WA[晶圆 Wafer<br/>放置在ESC表面]
               ESC[静电吸盘 ESC<br/>介电层: AlN/Al₂O₃<br/>加热层 → 基座 → 冷却通道<br/>类型: 库仑型/JR型]
               FR[聚焦环 Focus Ring<br/>材料: SiC/Si<br/>环绕晶圆外围]
               IR[绝缘环 Insulation Ring<br/>材料: Al₂O₃/SiO₂/石英<br/>防止等离子体泄漏]
               BE[下电极基座<br/>材料: Al<br/>连接RF电源]
           end

           subgraph 外部系统
               RF[RF电源系统<br/>高频: 27-60MHz 控制密度<br/>低频: 400K-2MHz 控制能量]
               MN[匹配网络<br/>L型或T型<br/>阻抗匹配]
               GAS[气体输送系统<br/>MFC + 混气室]
               VAC[真空系统<br/>干泵 + 涡轮分子泵 + 节流阀]
               TC[温控系统<br/>He背冷 + 水冷]
           end

           SH -->|垂直间距 30-50mm| WA
           UE -->|电场加速| P
           WA -->|放置在| ESC
           ESC -->|安装在| FR
           FR -->|环绕在| ESC
           BE -->|提供| RF
           GAS --> SH
           VAC -->|腔体底部抽气| P
       end

       style P fill:#e1f5ff
       style WA fill:#fff4e1
       style ESC fill:#ffe1e1
       style FR fill:#e1ffe1
       style SH fill:#d1e1ff

本章系统介绍电容耦合等离子体（CCP）刻蚀系统的完整架构、各子系统的详细工作原理、设计考量以及实际工程应用。CCP刻蚀系统是半导体制造中应用最广泛的刻蚀技术平台，尤其在介质刻蚀（氧化物、氮化物）领域占据主导地位。CCP以其高选择比、优异的形貌控制能力和成熟的产业化经验，在现代集成电路制造中发挥着不可替代的作用。

在半导体产线中，CCP机台的数量通常比ICP更多，因为后道工序（BEOL）需要不断进行薄膜沉积和刻蚀的重复步骤，而CCP正是处理介质材料和金属材料刻蚀的主力设备。
