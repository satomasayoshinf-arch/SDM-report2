#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
        def test_sample1(self):
                # 有効同値クラス：
                # 0 < A < B < 1000 を満たす整数
                # 正常系（R1: A < B）
                self.assertEqual(21, calc(3, 7))

        def test_sample2(self):
                # 無効同値クラス：
                # A ≤ 0 の場合（下限違反）
                # 条件 0 < A を満たさない
                self.assertEqual(-1, calc(0, 150))

        def test_sample3(self):
                # 無効同値クラス：
                # 数値以外の入力（型エラー相当）
                # 正規表現にマッチしないケース
                self.assertEqual(-1, calc('a', 'b'))

        def test_sample4(self):
                # 無効同値クラス：
                # 小数入力
                # 形式上は数値でも仕様上は棄却対象
                self.assertEqual(-1, calc(0.1, 999))

        def test_sample5(self):
                # 無効同値クラス：
                # A ≥ B の場合（関係条件違反）
                # R2: A = B
                self.assertEqual(-1, calc(5, 5))

        def test_sample6(self):
                # 無効同値クラス：
                # A > B の場合（関係条件違反）
                # R3: A > B
                self.assertEqual(-1, calc(10, 5))

        def test_sample7(self):
                # 無効同値クラス：
                # B ≥ 1000 の場合（上限違反）
                self.assertEqual(-1, calc(10, 1000))

        def test_sample8(self):
                # 無効同値クラス：
                # 負の値入力（0未満）
                # 正規表現で拒否、または数値条件違反
                self.assertEqual(-1, calc(-3, 10))

        def test_boundary_1(self):
                # 境界値：A = 0（下限そのもの）
                # 0 < A を満たさない
                self.assertEqual(-1, calc(0, 10))

        def test_boundary_2(self):
                # 境界値直後：A = 1（最小有効値）
                # 0 < 1 < 2 < 1000
                self.assertEqual(2, calc(1, 2))

        def test_boundary_3(self):
                # 境界値直前：A = -1（0未満）
                # 明確な下限違反
                self.assertEqual(-1, calc(-1, 10))

        def test_boundary_4(self):
                # 境界値：A = B
                # 条件 A < B を満たさない
                self.assertEqual(-1, calc(5, 5))

        def test_boundary_5(self):
                # 境界直前：A と B の差が最小（1差）
                # 有効な最小差ケース
                self.assertEqual(30, calc(5, 6))

        def test_boundary_6(self):
                # 境界値直前：B = 999（最大有効値）
                self.assertEqual(999, calc(1, 999))

        def test_boundary_7(self):
                # 境界値：B = 1000
                # B < 1000 を満たさない
                self.assertEqual(-1, calc(1, 1000))

        def test_boundary_8(self):
                # 境界値直後：B = 1001
                # 明確な上限違反
                self.assertEqual(-1, calc(1, 1001))
