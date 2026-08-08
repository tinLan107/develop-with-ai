# develop-with-ai

一套面向 Codex 与 AI 编程代理的证据优先开发标准流程。它的目标不是让 AI 更快地开始写代码，而是在写代码前尽量发现会导致返工、错误自动化或外部事故的真实需求，并用明确的阶段门控制设计、实现、集成、验证和发布。

## 它解决什么问题

- 需求在开发中途才被发现，导致界面、数据结构和业务逻辑反复重构。
- 只画了正常路径，却遗漏已有数据、重复操作、部分成功、结果不确定和失败恢复。
- 在外部 API、网页能力或真实业务样本尚未验证前就大规模开发。
- 把静态页面、模拟数据或一次成功误判为可发布能力。
- 把“分析与设计”误当成修改代码、数据或外部系统的授权。

## 核心方法

1. 先确认授权边界与风险等级。
2. 从真实工作样本重建当前流程（AS-IS）和目标流程（TO-BE）。
3. 盘点参与者、对象、动作、身份、数据源和外部依赖。
4. 建模对象生命周期，并明确历史数据如何接管。
5. 用操作矩阵覆盖正常、空数据、已有、重复、并发、失败、超时、取消、刷新、重启、部分成功和结果不确定。
6. 优先验证最可能推翻架构的高风险假设。
7. 按最小纵向切片开发，每一片都包含入口、规则、持久化、失败处理、恢复和验收。
8. 使用 `PASS / CONDITIONAL / BLOCKED` 阶段门决定是否继续，而不是凭“看起来能用”推进。

## 目录结构

```text
develop-with-ai/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── checklists.md
│   ├── model-selection.md
│   ├── requirements-discovery.md
│   ├── standards.md
│   └── workflow.md
└── scripts/
    └── validate_design_packet.py
```

仓库根目录的 README 用于项目介绍；真正可安装的 Skill 包位于 `develop-with-ai/` 目录中。

## 安装

```bash
git clone https://github.com/tinLan107/develop-with-ai.git
mkdir -p ~/.codex/skills
cp -R develop-with-ai/develop-with-ai ~/.codex/skills/develop-with-ai
```

安装后重新启动 Codex，或按当前 Codex 版本的 Skill 刷新方式重新载入。

## 使用

显式调用：

```text
使用 $develop-with-ai，先做需求发现和设计审计，暂不开发。
```

完整请求示例：

```text
使用 $develop-with-ai，先判断授权与风险等级；
用真实样本、对象生命周期、操作矩阵、历史数据和高风险假设完成需求发现门；
在我明确批准实施前，不要修改代码、数据或外部系统。
```

该 Skill 默认不允许隐式调用，避免普通讨论被误判为实施授权。

## 设计包校验

Skill 自带设计包校验脚本，可先运行自检：

```bash
python3 develop-with-ai/scripts/validate_design_packet.py --self-test
```

对已经生成的设计包执行校验时，请按脚本帮助信息提供目标路径：

```bash
python3 develop-with-ai/scripts/validate_design_packet.py --help
```

## 适用场景

- 新产品、新模块和内部运营系统的需求发现。
- 涉及数据库、历史数据、外部 API、网页自动化或真实写入的高风险开发。
- 已经出现多次返工，需要从流程层面阻止重复重构的项目。
- 在第一版发布前进行完整性、恢复能力和证据等级审计。

## 边界

- Skill 不替代业务负责人确认事实和优先级。
- 未获得明确授权时，只能分析、设计和验证，不应执行写入或删除。
- 对支付、发布、外部消息、生产数据和不可逆操作，仍应保留人工确认。
- 仓库当前未附加开源许可证；未经许可，不代表自动授予复制、修改或再发布权利。
