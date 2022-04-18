import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # type: ignore


def launch_chrome() -> webdriver.Chrome:
    # agrego esto por un bug extraño con puertos usb funcionando mal
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # hago global el driver asi el garbage collector no me lo borra cuando termina la func
    global driver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    driver.get("https://roc.myrb.io/s1/forms/M6I8P2PDOZFDBYYG")
    driver.implicitly_wait(5)
    try:
        assert driver.title == "Auditoria - R.O.C"
    except Exception:
        driver.close()
        raise Exception("La pagina no cargó correctamente el título Auditoria - R.O.C")
    return driver


def completar_proceso(proceso: str) -> None:
    if proceso == "Operaciones":
        driver.find_element(By.XPATH, '//*[@id="process"]/option[1]').click()
    elif proceso == "Cuentas por Cobrar":
        driver.find_element(By.XPATH, '//*[@id="process"]/option[2]').click()
    elif proceso == "Riesgo":
        driver.find_element(By.XPATH, '//*[@id="process"]/option[3]').click()
    elif proceso == "TI ":
        driver.find_element(By.XPATH, '//*[@id="process"]/option[4]').click()
    elif proceso == "Financiero":
        driver.find_element(By.XPATH, '//*[@id="process"]/option[5]').click()
    elif proceso == "Continuidad operacional":
        driver.find_element(By.XPATH, '//*[@id="process"]/option[6]').click()
    elif proceso == "Contabilidad":
        driver.find_element(By.XPATH, '//*[@id="process"]/option[8]').click()
    elif proceso == "Gobierno Corp":
        driver.find_element(By.XPATH, '//*[@id="process"]/option[9]').click()
    else:
        raise Exception(f"No se pudo encontrar el proceso {proceso}")


def completar_tipo_de_riesgo(tipo_de_riesgo: str) -> None:
    driver.find_element(By.XPATH, '//*[@id="tipo_riesgo"]').send_keys(
        f"{tipo_de_riesgo}" + Keys.TAB
    )


def completar_severidad(severidad: str) -> None:
    if severidad == "Alto":
        driver.find_element(By.XPATH, '//*[@id="severidad"]/option[1]').click()
    elif severidad == "Medio":
        driver.find_element(By.XPATH, '//*[@id="severidad"]/option[2]').click()
    elif severidad == "Bajo ":
        driver.find_element(By.XPATH, '//*[@id="severidad"]/option[3]').click()
    else:
        raise Exception(f"No se pudo encontrar la severidad de {severidad}")


def completar_responsable(responsable: str) -> None:
    driver.find_element(By.XPATH, '//*[@id="res"]').send_keys(
        f"{responsable}" + Keys.TAB
    )


def completar_fecha_de_compromiso(fecha_de_compromiso: datetime.datetime) -> None:
    day = str(fecha_de_compromiso.day)
    month = str(fecha_de_compromiso.month)
    year = str(fecha_de_compromiso.year)
    driver.find_element(By.XPATH, '//*[@id="date"]').send_keys(
        day + month + Keys.RIGHT + year
    )


def completar_observacion(observacion: str) -> None:
    driver.find_element(By.XPATH, '//*[@id="obs"]').send_keys(
        f"{observacion}" + Keys.TAB
    )


def submit_formulario() -> None:
    driver.find_element(By.XPATH, '//*[@id="submit"]').click()


def completar_form(
    proceso: str,
    tipo_de_riesgo: str,
    severidad: str,
    responsable: str,
    fecha_de_compromiso: datetime.datetime,
    observacion: str,
) -> None:
    print("llenando formulario")

    completar_proceso(proceso)
    completar_tipo_de_riesgo(tipo_de_riesgo)
    completar_severidad(severidad)
    completar_responsable(responsable)
    completar_fecha_de_compromiso(fecha_de_compromiso)
    completar_observacion(observacion)
    submit_formulario()


def main() -> None:
    print("corriendo local")
    launch_chrome()
    completar_form(
        proceso="Cuentas por Cobrar",
        tipo_de_riesgo="Riesgo Legal",
        severidad="Medio",
        responsable="Francisco Aguilera",
        fecha_de_compromiso=datetime.datetime.today(),
        observacion=" listado de clientes se encontraba desactualizado ",
    )
    # driver.quit()


if __name__ == "__main__":
    main()
