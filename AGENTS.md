# AGENTS.md

## 项目概述

基于 Python 的西北农林科技大学校园网自动登录程序，基于深澜校园网协议。

## 环境配置

- Python 3.12
- 使用 `uv` 管理虚拟环境和依赖：

```bash
uv venv --python 3.12
uv pip install -r requirements.txt
```

## 验证命令

```bash
python -m compileall NWAFU_WIFI_login loginScript.py always_online.py AutoLoad.py demo.py -q
python -c "from NWAFU_WIFI_login.LoginManager import LoginManager; print('IMPORT OK')"
python loginScript.py <username> <password>
```

## 构建系统

```bash
make confVenv    # 创建虚拟环境
make buildBinary # 构建可执行文件
make install     # 安装 systemd 服务和二进制
make clean       # 清理构建产物
```

## 代码规范

- `_decorators.py`、`LoginManager.py`、`srun_md5.py` 等文件保持原有 Tab 缩进，不要全文件格式化
- 不引入新的第三方依赖
- 不吞异常，至少打印异常信息
- 使用 `json.dumps` 而非字符串拼接构造 JSON
- 对 `re.search` 结果做 None 检查后再调用 `.group()`
