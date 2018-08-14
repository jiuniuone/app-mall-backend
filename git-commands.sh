#!/usr/bin/env bash
git clone <repository> --recursive 递归的方式克隆整个项目
git submodule add https://github.com/hikelee/acmin.git acmin 添加子模块
git submodule init 初始化子模块
git submodule update 更新子模块
git submodule foreach git pull 拉取所有子模块