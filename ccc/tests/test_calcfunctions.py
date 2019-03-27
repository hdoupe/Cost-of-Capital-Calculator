import pandas as pd
import numpy as np
import pytest
from pandas.testing import assert_frame_equal
from ccc import calcfunctions as cf


# def test_update_depr_methods(df, p):
#     test_df = cf.update_depr_methods(df, p)
#
#     assert_frame_equal(test_df, expected_df)
#


Y = np.array([40, 3, 10, 20, 8])
b = np.array([1.2, 1.0, 1.5, 2.0, 1.8])
bonus = np.array([0.0, 0.0, 0.4, 1.0, 0.9])
r = np.array([0.03, 0.03, 0.03, 0.03, 0.03])
expected_val = np.array([0.588563059, 0.956320164, 0.924042198, 1,
                         0.99041001])
test_data = [(Y, b, bonus, r, expected_val)]


@pytest.mark.parametrize('Y,b,bonus,r,expected_val', test_data,
                         ids=['Test 0'])
def test_dbsl(Y, b, bonus, r, expected_val):
    test_val = cf.dbsl(Y, b, bonus, r)

    assert(np.allclose(test_val, expected_val))


Y = np.array([40, 1, 10, 20, 8])
bonus = np.array([0, 0, 0.4, 1, 1.2])
r = np.array([0.12, 0.12, 0.12, 0.12, 0.12])
expected_val = np.array([0.206618803, 0.942329694, 0.749402894, 1,
                         1.071436018])
test_data = [(Y, bonus, r, expected_val)]


@pytest.mark.parametrize('Y,bonus,r,expected_val', test_data,
                         ids=['Test 0'])
def test_sl(Y, bonus, r, expected_val):
    test_val = cf.sl(Y, bonus, r)

    assert(np.allclose(test_val, expected_val))


delta = np.array([0.01, 0.1, 0.1, 0.02, 0.1])
bonus = np.array([0, 0, 0.4, 1, 1.2])
r = np.array([0.12, 0.12, 0.12, 0.12, 0.12])
pi = np.array([0.03, 0.03, 0.03, 0.03, 0.03])
expected_val = np.array([0.1, 0.526315789, 0.715789474, 1, 1.094736842])
test_data = [(delta, bonus, r, pi, expected_val)]


@pytest.mark.parametrize('delta,bonus,r,pi,expected_val', test_data,
                         ids=['Test 0'])
def test_econ(delta, bonus, r, pi, expected_val):
    test_val = cf.econ(delta, bonus, r, pi)

    assert(np.allclose(test_val, expected_val))


# def test_npv_tax_depr(df, r, pi):
#     test_df = cf.npv_tax_depr(df, r, pi)
#
#     assert_frame_equal(test_df, expected_df)


delta = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
z = np.array([0.1, 0, 0.5, 1, 0.55556, 0.8])
w = np.array([0.01, 0.01, 0.01, 0.01, 0.01, 0.01])
u = np.array([0.3, 0, 0.3, 0, 0.3, 0])
inv_tax_credit = np.array([0.08, 0.08, 0.08, 0.08, 0.08, 0.08])
pi = np.array([0.02, 0.02, 0.02, 0.02, 0.02, 0.02])
r = np.array([0.05, 0.06, 0.04, 0.03, 0.11, 0.12])

expected_val = np.array([0.075285714, 0.0388, 0.042, 0.0112,
                         0.114475829, 0.094])
test_data = [(delta, z, w, u, inv_tax_credit, pi, r, expected_val)]


@pytest.mark.parametrize('delta,z,w,u,inv_tax_credit,pi,r,expected_val',
                         test_data, ids=['Test 0'])
def test_eq_coc(delta, z, w, u, inv_tax_credit, pi, r, expected_val):
    test_val = cf.eq_coc(delta, z, w, u, inv_tax_credit, pi, r)

    assert(np.allclose(test_val, expected_val))


u = np.array([0.3, 0, 0.3, 0, 0.3, 0])
phi = np.array([0.33, 0.33, 0.33, 0.33, 0.33, 0.33])
Y_v = np.array([8, 8, 8, 8, 8, 8])
pi = np.array([0.02, 0.02, 0.02, 0.02, 0.02, 0.02])
r = np.array([0.05, 0.06, 0.04, 0.03, 0.11, 0.12])

expected_val = np.array([0.042779968, 0.04, 0.029723255, 0.01,
                         0.115882546, 0.1])
test_data = [(u, phi, Y_v, pi, r, expected_val)]


@pytest.mark.parametrize('u,phi,Y_v,pi,r,expected_val',
                         test_data, ids=['Test 0'])
def test_eq_coc_inventory(u, phi, Y_v, pi, r, expected_val):
    test_val = cf.eq_coc_inventory(u, phi, Y_v, pi, r)

    assert(np.allclose(test_val, expected_val))


rho = np.array([0.075285714, 0.0388, 0.042, 0.0112, 0.114475829, 0.094])
delta = np.array([0.05, 0.06, 0.04, 0.03, 0.11, 0.12])
expected_val = np.array([0.125285714, 0.0988, 0.082, 0.0412,
                         0.224475829, 0.214])
test_data = [(rho, delta, expected_val)]


@pytest.mark.parametrize('rho,delta,expected_val', test_data,
                         ids=['Test 0'])
def test_eq_ucc(rho, delta, expected_val):
    test_val = cf.eq_ucc(rho, delta)

    assert(np.allclose(test_val, expected_val))


rho = np.array([0.075285714, 0.0388, 0.042, 0.0112, 0.114475829, 0.094])
r_prime = np.array([0.05, 0.06, 0.04, 0.03, 0.11, 0.12])
pi = 0.02
expected_val = np.array([0.601518027, -0.030927835, 0.523809524,
                         0.107142857, 0.213807831, -0.063829787])
test_data = [(rho, r_prime, pi, expected_val)]


@pytest.mark.parametrize('rho,r_prime,pi,expected_val', test_data,
                         ids=['Test 0'])
def test_eq_metr(rho, r_prime, pi, expected_val):
    test_val = cf.eq_metr(rho, r_prime, pi)

    assert(np.allclose(test_val, expected_val))


rho = np.array([0.075285714, 0.0388, 0.042, 0.0112, 0.114475829, 0.094])
s = np.array([0.05, 0.06, 0.04, 0.03, 0.11, 0.12])
expected_val = np.array([0.335863378, -0.546391753, 0.047619048,
                         -1.678571429, 0.03909846, -0.276595745])
test_data = [(rho, s, expected_val)]


@pytest.mark.parametrize('rho,s,expected_val', test_data,
                         ids=['Test 0'])
def test_eq_mettr(rho, s, expected_val):
    test_val = cf.eq_mettr(rho, s)

    assert(np.allclose(test_val, expected_val))


rho = np.array([0.075285714, 0.0388, 0.042, 0.0112, 0.114475829, 0.094])
s = np.array([0.05, 0.06, 0.04, 0.03, 0.11, 0.12])
expected_val = np.array([0.02528571, -0.0212, 0.002, -0.0188,
                         0.00447583, -0.026])
test_data = [(rho, s, expected_val)]


@pytest.mark.parametrize('rho,s,expected_val', test_data,
                         ids=['Test 0'])
def test_eq_tax_wedge(rho, s, expected_val):
    test_val = cf.eq_tax_wedge(rho, s)

    assert(np.allclose(test_val, expected_val))


rho = np.array([0.075285714, 0.0388, 0.042, 0.0112, 0.114475829, 0.094])
metr = np.array([0.601518027, -0.030927835, 0.523809524, 0.107142857,
                 0.213807831, -0.063829787])
profit_rate = np.array([0.1, 0.2, 0.3, 0.05, 0.5, 1])
u = np.array([0.35, 0.21, 0, 0.4, 1, 0.9])
expected_val = np.array([0.539357143, 0.16326, 0.073333333, 0.3344,
                         0.82, 0.8094])
test_data = [(rho, metr, profit_rate, u, expected_val)]


@pytest.mark.parametrize('rho,metr,profit_rate,u,expected_val', test_data,
                         ids=['Test 0'])
def test_eq_eatr(rho, metr, profit_rate, u, expected_val):
    test_val = cf.eq_eatr(rho, metr, profit_rate, u)

    assert(np.allclose(test_val, expected_val))
