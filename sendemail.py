from dotenv import load_dotenv
import os
import datetime
import yagmail  # type: ignore


def configurar_servidor() -> None:
    load_dotenv("myvars.env")

    email_de = os.getenv("EMAIL_DE")
    password = os.getenv("PASSWORD")

    global yag
    yag = yagmail.SMTP(user=email_de, password=password)


def enviar_email(
    email_para: str,
    proceso: str,
    estado: str,
    fecha_de_compromiso: datetime.datetime,
    observacion: str,
) -> None:
    print("enviando email")

    message = f"""
Hola! Este es un email automático.
Usted tiene el proceso {proceso} en el estado {estado},
{observacion} y tiene una fecha de compromiso {fecha_de_compromiso.strftime('%d de %B de %Y')}"""
    asunto = "Email automatico de Rocketbot"
    yag.send(
        to=email_para, subject=asunto, contents=message, cc="forosypaginas@gmail.com"
    )


def cerrar_servidor() -> None:
    yag.close()


def main() -> None:
    print("enviando email de forma local")
    configurar_servidor()
    enviar_email(
        email_para="Francisco.Aguilera_yyy1234@Hotmail.com",
        proceso="Cuentas por Cobrar",
        estado="Atrasado",
        fecha_de_compromiso=datetime.datetime.today(),
        observacion="errores en inscripción",
    )
    cerrar_servidor()


if __name__ == "__main__":
    main()
