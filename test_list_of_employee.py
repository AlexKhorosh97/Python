import requests
import pytest
import psycopg2
from EmployeeDB import EmployerTable

db = EmployerTable("postgresql://Александр Хорошев:0158@localhost:5432/mydatabase")


def test_get_list():
    name = "My company"
    db.create_company(name)
    max_id = db.get_max_id_comp()

    
    db_result = db.select_employers(max_id)
    db.delete_company(max_id)
    assert len == len(db_result)


def test_add_new_employer():
    db.create_company('Моя компания')
    max_id_c = db.get_max_id_comp()
    db_result_b = db.select_employers(max_id_c)

    f_name = 'Иван'
    l_name = 'Петров'
    phone = '+79969598584'

    db.create_employer(max_id_c, f_name, l_name, phone)
    db_result_a = db.select_employers(max_id_c)

    assert len == len(db_result_b)
    assert len == len(db_result_a)
    assert len(db_result_a) - len(db_result_b) == 1
    

    db.clear_table_employers(max_id_c)
    db.delete_company(max_id_c)


def test_one_employer():
    db.create_company('Моя компания')
    max_id_c = db.get_max_id_comp()

    name_emp = 'Иван'
    la_name = 'Петров'
    phone_num = '+79969598584'

    db.create_employer(max_id_c, name_emp, la_name, phone_num)
    max_id_e = db.get_max_id_emp(max_id_c)
    db_result = db.get_employer_by_id(max_id_e)

    assert db_result["firstName"] == name_emp
    assert db_result["lastName"] == la_name
    assert db_result["companyId"] == max_id_c
    assert db_result["phone"] == phone_num

    db.clear_table_employers(max_id_c)
    db.delete_company(max_id_c)


def test_change_data():
    db.create_company('Моя компания')
    max_id_c = db.get_max_id_comp()

    name_emp = 'Иван'
    la_name = 'Петров'
    phone_num = '+79969598584'

    db.create_employer(max_id_c, name_emp, la_name, phone_num)
    max_id_e = db.get_max_id_emp(max_id_c)
    

    id = max_id_e
    last_name = 'Белов'
    email = 'test@mail.com'
    url = 'https://my_profile.com'
    phone = '89654789654'
    is_active = True

    db.clear_table_employers(max_id_c)
    db.delete_company(max_id_c)


def test_delete_company_and_employers():
    name = 'Моя компания'
    db.create_company(name)
    max_id_c = db.get_max_id_comp()

    name_emp = 'Иван'
    la_name = 'Петров'
    phone_num = '+79969598584'

    db.create_employer(max_id_c, name_emp, la_name, phone_num)
    db.clear_table_employers(max_id_c)
    deleted = db.delete_company(max_id_c)

    assert deleted["id"] == max_id_c
    assert deleted["name"] == name
    assert deleted["isActive"] == True
