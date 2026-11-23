#!/usr/bin/env python3
"""D34 CI 实战：流水线里跑的单元测试（纯标准库，零依赖）"""
import os
import sys


def test_index_exists():
    assert os.path.isfile("app/index.html"), "app/index.html 不存在"
    print("[PASS] test_index_exists: 首页文件存在")


def test_index_content():
    with open("app/index.html", encoding="utf-8") as f:
        content = f.read()
    assert "CI/CD" in content, "首页缺少 CI/CD 标记"
    assert "v1.0.0" in content, "首页缺少版本号"
    print("[PASS] test_index_content: 首页内容正确")


def test_dockerfile():
    assert os.path.isfile("Dockerfile"), "Dockerfile 不存在"
    with open("Dockerfile", encoding="utf-8") as f:
        d = f.read()
    assert "FROM" in d and "nginx" in d, "Dockerfile 基础镜像不对"
    print("[PASS] test_dockerfile: Dockerfile 合法")


if __name__ == "__main__":
    tests = [test_index_exists, test_index_content, test_dockerfile]
    failed = 0
    for t in tests:
        try:
            t()
        except AssertionError as e:
            print(f"[FAIL] {t.__name__}: {e}")
            failed += 1
    if failed:
        print(f"\n结果: {failed} 个测试失败")
        sys.exit(1)
    print(f"\n结果: 全部 {len(tests)} 个测试通过 ✅")
