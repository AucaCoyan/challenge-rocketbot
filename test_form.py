import pytest
import form
import datetime
from selenium.webdriver.common.by import By


defaults = {
    "proceso": "Cuentas por Cobrar",
    "tipo_de_riesgo": "Riesgo Legal",
    "severidad": "Alto",
    "responsable": "Francisco Aguilera",
    "fecha_de_compromiso": datetime.datetime.today(),
    "observacion": " listado de clientes se encontraba desactualizado ",
}

driver = form.launch_chrome()


# Esta funcion lo que esta haciendo es verificar si en html
# el <option 1 == Alto>, lo cual siempre va ser verdadero
# por lo tanto no testea si la funcion anda correctamente
@pytest.mark.parametrize("severidad", ["Alto", "Medio", "Baja "])
def test_severidad_medio(severidad: str) -> None:
    form.completar_form(
        proceso=defaults["proceso"],
        tipo_de_riesgo=defaults["tipo_de_riesgo"],
        severidad=severidad,
        responsable=defaults["responsable"],
        fecha_de_compromiso=defaults["fecha_de_compromiso"],
        observacion=defaults["observacion"],
    )
    if severidad == "Alto":
        assert (
            driver.find_element(By.XPATH, '//*[@id="severidad"]/option[1]').text
            == "Alto"
        )
    elif severidad == "Medio":
        assert (
            driver.find_element(By.XPATH, '//*[@id="severidad"]/option[2]').text
            == "Medio"
        )
    elif severidad == "Baja ":
        assert (
            driver.find_element(By.XPATH, '//*[@id="severidad"]/option[3]').text
            == "Bajo"
        )


"""     element = driver.find_element(By.XPATH, '//*[@id="severidad"]')
    print(element.get_attribute("value"))
    print(element.tag_name)
    print(element.text)
    assert element.get_attribute("value") == f"{severidad}" """
