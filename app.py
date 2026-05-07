print("DIAGNÓSTICO EMPRESARIAL - ÁREA ADMINISTRATIVA/ORGANIZACIONAL")
print("Este cuestionario tiene como objetivo evaluar el nivel de madurez de un emprendimiento en seis áreas clave: legal, administrativa, comercial, financiera, técnica y ecológica. No existen respuestas correctas o incorrectas. Responde con honestidad para obtener un diagnóstico útil.")
print("Escala: 1 = No existe, 2 = Existe de manera informal, 3 = Existe parcialmente, 4 = Existe y funciona adecuadamente, 5 = Existe y está documentado\n")

total_admin = 0
import streamlit as st
total_admin += st.selectbox("1. ¿Cuenta con estructura organizacional definida?", [1,2,3,4,5])
total_admin += st.selectbox("2. ¿Están claros los roles y responsabilidades?", [1,2,3,4,5])
total_admin += st.selectbox("3. ¿Existe un responsable de decisiones clave?", [1,2,3,4,5])
total_admin += st.selectbox("4. ¿Los socios tienen funciones diferenciadas?", [1,2,3,4,5])
total_admin += st.selectbox("5. ¿Las decisiones se documentan?", [1,2,3,4,5])
total_admin += st.selectbox("6. ¿Existen procesos definidos para actividades clave?", [1,2,3,4,5])
total_admin += st.selectbox("7. ¿Los procesos están documentados?", [1,2,3,4,5])
total_admin += st.selectbox("8. ¿Se usan herramientas de seguimiento de tareas?", [1,2,3,4,5])
total_admin += st.selectbox("9. ¿Se mide el desempeño periódicamente?", [1,2,3,4,5])
total_admin += st.selectbox("10. ¿Existen indicadores administrativos?", [1,2,3,4,5])
total_admin += st.selectbox("11. ¿Tiene objetivos claros a corto y mediano plazo?", [1,2,3,4,5])
total_admin += st.selectbox("12. ¿Realiza planeación anual o semestral?", [1,2,3,4,5])
total_admin += st.selectbox("13. ¿Revisa resultados contra lo planeado?", [1,2,3,4,5])
total_admin += st.selectbox("14. ¿Ajusta estrategias cuando algo no funciona?", [1,2,3,4,5])
total_admin += st.selectbox("15. ¿El negocio depende de una sola persona?", [1,2,3,4,5])
total_admin += st.selectbox("16. ¿Cuenta con personal formal?", [1,2,3,4,5])
total_admin += st.selectbox("17. ¿Hay claridad en horarios y pagos?", [1,2,3,4,5])
total_admin += st.selectbox("18. ¿Se capacita al personal regularmente?", [1,2,3,4,5])
total_admin += st.selectbox("19. ¿Existe alta rotación de personal?", [1,2,3,4,5])
total_admin += st.selectbox("20. ¿El clima organizacional es favorable?", [1,2,3,4,5])

st.write("\nPuntaje total área administrativa:", total_admin)

if total_admin <= 30:
    st.write("Nivel PRINCIPIANTE: estructura necesidad")
elif total_admin <= 55:
    st.write("Nivel INTERMEDIO: estructura oportunidad")
elif total_admin <= 70:
    st.write("Nivel AVANZADO: estructura funcional")
else:
    st.write("Nivel EXPERTO: estructura estratégico")
    
st.write("\nDIAGNÓSTICO EMPRESARIAL - ÁREA COMERCIAL")
st.write("Escala: 1 = No existe, 2 = Informal, 3 = Parcial, 4 = Funciona, 5 = Documentado\n")

total_comercial = 0

total_comercial += st.selectbox("21. ¿Tiene definida su propuesta de valor?", [1,2,3,4,5])
total_comercial += st.selectbox("22. ¿Resuelve un problema real del cliente?", [1,2,3,4,5])
total_comercial += st.selectbox("23. ¿Tiene identificado a su cliente objetivo?", [1,2,3,4,5])
total_comercial += st.selectbox("24. ¿Conoce el perfil del cliente ideal?", [1,2,3,4,5])
total_comercial += st.selectbox("25. ¿Se diferencia de la competencia?", [1,2,3,4,5])
total_comercial += st.selectbox("26. ¿Cuenta con canales de venta definidos?", [1,2,3,4,5])
total_comercial += st.selectbox("27. ¿Los canales actuales son efectivos?", [1,2,3,4,5])
total_comercial += st.selectbox("28. ¿Existe un proceso de ventas estructurado?", [1,2,3,4,5])
total_comercial += st.selectbox("29. ¿Mide la conversión de prospectos?", [1,2,3,4,5])
total_comercial += st.selectbox("30. ¿Da seguimiento a clientes potenciales?", [1,2,3,4,5])
total_comercial += st.selectbox("31. ¿El modelo de ingresos está definido?", [1,2,3,4,5])
total_comercial += st.selectbox("32. ¿Los precios cubren costos y generan utilidad?", [1,2,3,4,5])
total_comercial += st.selectbox("33. ¿Revisa precios periódicamente?", [1,2,3,4,5])
total_comercial += st.selectbox("34. ¿Depende de pocos clientes?", [1,2,3,4,5])
total_comercial += st.selectbox("35. ¿Los ingresos son recurrentes?", [1,2,3,4,5])
total_comercial += st.selectbox("36. ¿Realiza acciones de marketing constantes?", [1,2,3,4,5])
total_comercial += st.selectbox("37. ¿Utiliza medios digitales para vender?", [1,2,3,4,5])
total_comercial += st.selectbox("38. ¿Mide la satisfacción del cliente?", [1,2,3,4,5])
total_comercial += st.selectbox("39. ¿Cuenta con estrategias de fidelización?", [1,2,3,4,5])
total_comercial += st.selectbox("40. ¿La marca es reconocible en su mercado?", [1,2,3,4,5])

st.write("\nPuntaje total área comercial:", total_comercial)

if total_comercial <= 30:
    st.write("Nivel PRINCIPIANTE: comercial necesidad")
elif total_comercial <= 55:
    st.write("Nivel INTERMEDIO: comercial oportunidad")
elif total_comercial <= 70:
    st.write("Nivel AVANZADO: comercial funcional")
else:
    st.write("Nivel EXPERTO: comercial estratégica")
    
st.write("\nDIAGNÓSTICO EMPRESARIAL - ÁREA FINANCIERA")
st.write("Escala: 1 = No existe, 2 = Informal, 3 = Parcial, 4 = Funciona, 5 = Documentado\n")

total_financiera = 0

total_financiera += st.selectbox("41. ¿Lleva registros financieros formales?", [1,2,3,4,5])
total_financiera += st.selectbox("42. ¿Elabora estados financieros periódicos?", [1,2,3,4,5])
total_financiera += st.selectbox("43. ¿Separa finanzas personales y del negocio?", [1,2,3,4,5])
total_financiera += st.selectbox("44. ¿Conoce su flujo de efectivo mensual?", [1,2,3,4,5])
total_financiera += st.selectbox("45. ¿Identifica ingresos y egresos claramente?", [1,2,3,4,5])
total_financiera += st.selectbox("46. ¿El negocio es rentable actualmente?", [1,2,3,4,5])
total_financiera += st.selectbox("47. ¿Conoce sus costos fijos y variables?", [1,2,3,4,5])
total_financiera += st.selectbox("48. ¿Calcula su punto de equilibrio?", [1,2,3,4,5])
total_financiera += st.selectbox("49. ¿Analiza márgenes de utilidad?", [1,2,3,4,5])
total_financiera += st.selectbox("50. ¿Identifica fugas de dinero?", [1,2,3,4,5])
total_financiera += st.selectbox("51. ¿Cuenta con liquidez suficiente?", [1,2,3,4,5])
total_financiera += st.selectbox("52. ¿Ha utilizado financiamiento externo?", [1,2,3,4,5])
total_financiera += st.selectbox("53. ¿Las deudas son manejables?", [1,2,3,4,5])
total_financiera += st.selectbox("54. ¿Conoce el costo de su financiamiento?", [1,2,3,4,5])
total_financiera += st.selectbox("55. ¿Tiene planeación para contingencias?", [1,2,3,4,5])
total_financiera += st.selectbox("56. ¿Cuenta con proyecciones financieras?", [1,2,3,4,5])
total_financiera += st.selectbox("57. ¿Analiza escenarios de crecimiento?", [1,2,3,4,5])
total_financiera += st.selectbox("58. ¿Reinvierte utilidades en el negocio?", [1,2,3,4,5])
total_financiera += st.selectbox("59. ¿Evalúa inversiones antes de ejecutarlas?", [1,2,3,4,5])
total_financiera += st.selectbox("60. ¿Puede crecer sin comprometer estabilidad financiera?", [1,2,3,4,5])

st.write("\nPuntaje total área financiera:", total_financiera)

if total_financiera <= 30:
    st.write("Nivel PRINCIPIANTE: financiera necesidad")
elif total_financiera <= 55:
    st.write("Nivel INTERMEDIO: financiera oportunidad")
elif total_financiera <= 70:
    st.write("Nivel AVANZADO: financiera funcional")
else:
    st.write("Nivel EXPERTO: financiera estratégica")

st.write("\nDIAGNÓSTICO EMPRESARIAL - ÁREA TÉCNICA")
st.write("Escala: 1 = No existe, 2 = Informal, 3 = Parcial, 4 = Funciona, 5 = Documentado\n")

total_técnica = 0

total_técnica += st.selectbox("61. ¿Domina técnicamente su producto o servicio?", [1,2,3,4,5])
total_técnica += st.selectbox("62. ¿Tiene procesos técnicos definidos?", [1,2,3,4,5])
total_técnica += st.selectbox("63. ¿La calidad es consistente?", [1,2,3,4,5])
total_técnica += st.selectbox("64. ¿Cuenta con estándares de calidad?", [1,2,3,4,5])
total_técnica += st.selectbox("65. ¿La operación depende de una persona clave?", [1,2,3,4,5])
total_técnica += st.selectbox("66. ¿Utiliza tecnología adecuada?", [1,2,3,4,5])
total_técnica += st.selectbox("67. ¿La infraestructura es suficiente?", [1,2,3,4,5])
total_técnica += st.selectbox("68. ¿Existen cuellos de botella operativos?", [1,2,3,4,5])
total_técnica += st.selectbox("69. ¿La operación es escalable?", [1,2,3,4,5])
total_técnica += st.selectbox("70. ¿Aplica mejoras continuas?", [1,2,3,4,5])
total_técnica += st.selectbox("71. ¿Documenta fallas operativas?", [1,2,3,4,5])
total_técnica += st.selectbox("72. ¿Aplica acciones correctivas?", [1,2,3,4,5])
total_técnica += st.selectbox("73. ¿La capacidad instalada cubre la demanda?", [1,2,3,4,5])
total_técnica += st.selectbox("74. ¿Planea la operación a futuro?", [1,2,3,4,5])
total_técnica += st.selectbox("75. ¿La operación es replicable?", [1,2,3,4,5])

st.write("\nPuntaje total área técnica/operativa:", total_técnica)

if total_técnica <= 22:
    st.write("Nivel PRINCIPIANTE: técnica necesidad")
elif total_técnica <= 41:
    st.write("Nivel INTERMEDIO: técnica oportunidad")
elif total_técnica <= 53:
    st.write("Nivel AVANZADO: técnica funcional")
else:
    st.write("Nivel EXPERTO: técnica estratégica")

st.write("\nDIAGNÓSTICO EMPRESARIAL - ÁREA ECOLÓGICA")
st.write("Escala: 1 = No existe, 2 = Informal, 3 = Parcial, 4 = Funciona, 5 = Documentado\n")

total_ecológica = 0

total_ecológica += st.selectbox("76. ¿Identifica su impacto ambiental?", [1,2,3,4,5])
total_ecológica += st.selectbox("77. ¿Minimiza el uso de recursos no renovables?", [1,2,3,4,5])
total_ecológica += st.selectbox("78. ¿Gestiona adecuadamente sus residuos?", [1,2,3,4,5])
total_ecológica += st.selectbox("79. ¿Promueve el uso responsable de insumos?", [1,2,3,4,5])
total_ecológica += st.selectbox("80. ¿Cumple normativas ambientales aplicables?", [1,2,3,4,5])
total_ecológica += st.selectbox("81. ¿Aplica prácticas de sostenibilidad?", [1,2,3,4,5])
total_ecológica += st.selectbox("82. ¿Comunica su compromiso ambiental?", [1,2,3,4,5])
total_ecológica += st.selectbox("83. ¿Busca eficiencia energética?", [1,2,3,4,5])
total_ecológica += st.selectbox("84. ¿Evalúa impacto ecológico al crecer?", [1,2,3,4,5])
total_ecológica += st.selectbox("85. ¿La sostenibilidad es parte de su estrategia?", [1,2,3,4,5])

st.write("\nPuntaje total área ecológica:", total_ecológica)

if total_ecológica <= 15:
    st.write("Nivel PRINCIPIANTE: ecológica necesidad")
elif total_ecológica <= 27:
    st.write("Nivel INTERMEDIO: ecológica oportunidad")
elif total_ecológica <= 35:
    st.write("Nivel AVANZADO: ecológica funcional")
else:
    st.write("Nivel EXPERTO: ecológica estratégica")

st.write("\nDIAGNÓSTICO EMPRESARIAL - ÁREA LEGAL")
st.write("Escala: 1 = No existe, 2 = Informal, 3 = Parcial, 4 = Funciona, 5 = Documentado\n")

total_legal = 0

total_legal += st.selectbox("86. ¿El negocio está legalmente constituido?", [1,2,3,4,5])
total_legal += st.selectbox("87. ¿Opera como persona física o moral acorde a su actividad?", [1,2,3,4,5])
total_legal += st.selectbox("88. ¿La figura legal es congruente con el giro del negocio?", [1,2,3,4,5])
total_legal += st.selectbox("89. ¿Cuenta con acta constitutiva vigente (si aplica)?", [1,2,3,4,5])
total_legal += st.selectbox("90. ¿Los socios están correctamente registrados?", [1,2,3,4,5])
total_legal += st.selectbox("91. ¿Está dado de alta ante el SAT?", [1,2,3,4,5])
total_legal += st.selectbox("92. ¿El régimen fiscal corresponde a su actividad real?", [1,2,3,4,5])
total_legal += st.selectbox("93. ¿Emite facturas por todos sus ingresos?", [1,2,3,4,5])
total_legal += st.selectbox("94. ¿Presenta declaraciones fiscales en tiempo y forma?", [1,2,3,4,5])
total_legal += st.selectbox("95. ¿Tiene adeudos fiscales pendientes?", [1,2,3,4,5])
total_legal += st.selectbox("96. ¿Cuenta con contratos formales con proveedores?", [1,2,3,4,5])
total_legal += st.selectbox("97. ¿Cuenta con contratos con clientes cuando es necesario?", [1,2,3,4,5])
total_legal += st.selectbox("98. ¿Existen convenios o acuerdos entre socios?", [1,2,3,4,5])
total_legal += st.selectbox("99. ¿Están definidas las responsabilidades legales de cada socio?", [1,2,3,4,5])
total_legal += st.selectbox("100. ¿Existen cláusulas de salida o disolución?", [1,2,3,4,5])
total_legal += st.selectbox("101. ¿Cuenta con licencias o permisos para operar?", [1,2,3,4,5])
total_legal += st.selectbox("102. ¿Cumple con normativas aplicables?", [1,2,3,4,5])
total_legal += st.selectbox("103. ¿Tiene identificados riesgos legales actuales?", [1,2,3,4,5])
total_legal += st.selectbox("104. ¿Cuenta con asesoría legal de respaldo?", [1,2,3,4,5])
total_legal += st.selectbox("105. ¿La estructura legal permite el crecimiento del negocio?", [1,2,3,4,5])

st.write("\nPuntaje total área legal:", total_legal)

if total_legal <= 30:
    st.write("Nivel PRINCIPIANTE: legal necesidad")
elif total_legal <= 55:
    st.write("Nivel INTERMEDIO: legal oportunidad")
elif total_legal <= 70:
    st.write("Nivel AVANZADO: legal funcional")
else:
    st.write("Nivel EXPERTO: legal estratégica")

st.write("\nDIAGNÓSTICO EMPRESARIAL - RESUMEN")

st.write("\nÁrea Administrativa:", total_admin)
if total_admin <= 30:
    st.write("Nivel PRINCIPIANTE: estructura necesidad")
elif total_admin <= 55:
    st.write("Nivel INTERMEDIO: estructura oportunidad")
elif total_admin <= 70:
    st.write("Nivel AVANZADO: estructura funcional")
else:
    st.write("Nivel EXPERTO: estructura estratégico")
if total_admin <= 30:
    st.write("""En este nivel Principiante, el negocio opera sin una estructura organizacional clara, lo que implica que las decisiones, los procesos y las responsabilidades no están formalmene definidos y dependen en gran medida de una sola persona. La ausencia de procesos documentados, indicadores y planeación provoca que la operación funcione más por esfuerzo personal que por un sistema establecido, generando desorden y limitando la capacidad de crecimiento. Esta situación representa un alto riesgo operativo, ya que dificulta la delegación, incrementa la carga del dueño y puede derivar en ineficiencias constantes. En términos prácticos, el negocio sí existe y opera, pero aún no cuenta con una base organizacional sólida que le permita sostenerse y evolucionar de manera estructurada.""")
elif total_admin <= 55:
    st.write("""En este nivel Intermedio, el negocio cuenta con ciertos elementos de estructura que le permiten operar, sin embargo, aún no logra mantener un control consistente sobre sus procesos y resultados. Existen avances como la definición parcial de roles, algunos procesos en marcha y ciertos intentos de medición, pero estos no están documentados ni se aplican de manera uniforme. La planeación puede estar presente, aunque no siempre se sigue, y los ajustes suelen realizarse de forma reactiva ante los problemas. Esta situación genera un crecimiento desordenado, desgaste operativo e inconsistencias en los resultados. En términos prácticos, el negocio muestra intención de organización, pero aún no ha consolidado una estructura que le permita operar con estabilidad y control.""")
elif total_admin <= 70:
   st.write("""En este nivel Avanzado, el negocio ha logrado establecer una estructura funcional que le permite operar con orden y cierto grado de control. Cuenta con procesos definidos y en uso, roles claros en la mayoría del equipo, así como indicadores que permiten dar seguimiento a su desempeño. La planeación se realiza de forma periódica y existe un seguimiento operativo constante que favorece la estabilidad del negocio. Esto indica que la operación ya no depende únicamente del esfuerzo individual, sino de un sistema organizado. Sin embargo, existe el riesgo de estancamiento si no se continúa evolucionando y optimizando. En términos prácticos, el negocio funciona adecuadamente y cuenta con bases sólidas, pero requiere avanzar hacia un enfoque más estratégico para seguir creciendo.""")
else:
    st.write("""En este nivel Experto, el negocio cuenta con una estructura organizacional completamente definida que le permite no solo operar, sino también escalar y sostener su crecimiento. Los procesos están documentados y son replicables, los indicadores son claros y se utilizan activamente para la toma de decisiones, y existe una planeación estratégica que guía el rumbo del negocio. Además, se observa una cultura organizacional estable que facilita la delegación y el desarrollo del equipo. Esta estructura convierte al negocio en un sistema preparado para expandirse de manera ordenada. No obstante, implica el reto de gestionar una mayor complejidad y mantener una evolución constante. En términos prácticos, la organización no solo sostiene la operación, sino que impulsa activamente su crecimiento y posicionamiento.""")

st.write("\nÁrea Comercial:", total_comercial)
if total_comercial <= 30:
    st.write("Nivel PRINCIPIANTE: comercial necesidad")
elif total_comercial <= 55:
    st.write("Nivel INTERMEDIO: comercial oportunidad")
elif total_comercial <= 70:
    st.write("Nivel AVANZADO: comercial funcional")
else:
    st.write("Nivel EXPERTO: comercial estratégica")
if total_comercial <= 30:
    st.write("""En este nivel Principiante, el negocio no cuenta con una estructura comercial definida, lo que implica que la propuesta de valor, el cliente objetivo y los canales de venta no están claramente establecidos. La generación de ingresos depende de esfuerzos aislados y no de un proceso de ventas estructurado, lo que provoca resultados inconsistentes y poco predecibles. La ausencia de estrategias de marketing, seguimiento a clientes y medición de resultados limita la capacidad de crecimiento. Esta situación representa un alto riesgo comercial, ya que dificulta la generación de ingresos estables y sostenibles. En términos prácticos, el negocio puede vender en ciertos momentos, pero aún no cuenta con un sistema comercial sólido que le permita sostener y escalar sus ingresos de manera estructurada.""")
elif total_comercial <= 55:
    st.write("""En este nivel Intermedio, el negocio cuenta con ciertos elementos comerciales que le permiten generar ingresos, sin embargo, aún no logra mantener un control consistente sobre su proceso de ventas y sus resultados. Existen avances como una propuesta de valor básica, algunos canales de venta activos y cierto conocimiento del cliente, pero estos elementos no están completamente definidos ni operan de manera uniforme. Las acciones de marketing y el seguimiento a clientes suelen ser irregulares, lo que provoca ingresos variables y dificulta la estabilidad del negocio. Esta situación representa un riesgo comercial, ya que limita el aprovechamiento de oportunidades y el crecimiento sostenido. En términos prácticos, el negocio tiene capacidad de vender, pero aún no ha consolidado un sistema comercial estructurado que le permita generar ingresos de manera constante y predecible.""")
elif total_comercial <= 70:
   st.write("""En este nivel Avanzado, el negocio ha logrado estructurar un sistema comercial funcional que le permite generar ingresos de manera constante y con cierto nivel de control. Cuenta con una propuesta de valor clara, identifica a su cliente objetivo y utiliza canales de venta definidos que contribuyen a la generación de resultados. Además, existe un proceso de ventas establecido, se da seguimiento a clientes potenciales y se implementan acciones de marketing de forma regular. Esto permite que los ingresos sean más estables y predecibles. Sin embargo, aún existe oportunidad de optimizar y escalar el sistema comercial. En términos prácticos, el negocio vende de manera consistente, pero requiere evolucionar hacia un enfoque más estratégico para potenciar su crecimiento.""")
else:
    st.write("""En este nivel Experto, el negocio cuenta con una estructura comercial sólida, optimizada y orientada estratégicamente al crecimiento. La propuesta de valor está claramente posicionada, el cliente ideal se encuentra bien definido y segmentado, y los canales de venta son efectivos y escalables. El proceso comercial se encuentra estructurado y medido, permitiendo analizar la conversión de prospectos, dar seguimiento sistemático a clientes y aplicar estrategias de fidelización. Además, se mide la satisfacción del cliente y los ingresos son recurrentes y sostenibles. Esta capacidad permite que el negocio no solo genere ventas, sino que gestione estratégicamente su crecimiento en el mercado. En términos prácticos, el sistema comercial no solo sostiene la operación, sino que impulsa activamente la expansión y posicionamiento del negocio.""") 

st.write("\nÁrea Financiera:", total_financiera)
if total_financiera <= 30:
    st.write("Nivel PRINCIPIANTE: financiera necesidad")
elif total_financiera <= 55:
    st.write("Nivel INTERMEDIO: financiera oportunidad")
elif total_financiera <= 70:
    st.write("Nivel AVANZADO: financiera funcional")
else:
    st.write("Nivel EXPERTO: financiera estratégica")
if total_financiera <= 30:
    st.write("""En este nivel Principiante, el negocio no cuenta con una estructura financiera definida, lo que implica que no tiene claridad sobre su flujo de efectivo, sus costos ni su rentabilidad. La ausencia de registros financieros formales y de estados financieros periódicos impide tener visibilidad sobre su situación económica, mientras que la mezcla entre finanzas personales y del negocio genera desorden en el uso de los recursos. Esta falta de control limita la toma de decisiones y aumenta el riesgo de pérdidas no detectadas y problemas de liquidez. En términos prácticos, el negocio puede generar ingresos, pero no cuenta con una base financiera que le permita entender su desempeño ni sostener su operación de manera estructurada.""")
elif total_financiera <= 55:
    st.write("""En este nivel Intermedio, el negocio cuenta con ciertos elementos financieros que le permiten tener una visión parcial de su situación, sin embargo, aún no logra mantener un control consistente sobre sus recursos ni sobre sus resultados. Existen algunos registros y reportes, pero no están completos ni actualizados, y el análisis financiero se realiza de manera irregular. La separación entre finanzas personales y del negocio es parcial, lo que genera desorden en la administración del dinero. Esta falta de consistencia limita la toma de decisiones y aumenta el riesgo de errores financieros y problemas de liquidez. En términos prácticos, el negocio comienza a entender sus finanzas, pero aún no ha consolidado un sistema que le permita controlarlas y utilizarlas de forma estratégica.""")
elif total_financiera <= 70:
   st.write("""En este nivel Avanzado, el negocio ha logrado establecer una estructura financiera funcional que le permite operar con control y tomar decisiones con base en información confiable. Cuenta con registros financieros formales, estados financieros periódicos y una clara separación entre las finanzas personales y las del negocio. Se monitorea el flujo de efectivo, se identifican costos y márgenes, y se realizan análisis que favorecen la estabilidad operativa. Sin embargo, aún existe oportunidad de optimizar y evolucionar hacia un enfoque más estratégico. En términos prácticos, el negocio cuenta con bases financieras sólidas que le permiten sostener su operación, pero requiere fortalecer su análisis y planeación para impulsar su crecimiento.""")
else:
    st.write("""En este nivel Experto, el negocio cuenta con una estructura financiera sólida, completa y orientada estratégicamente al crecimiento. Los registros son precisos y actualizados, los estados financieros se analizan de forma periódica y existe un control total del flujo de efectivo. Se optimizan costos, márgenes y rentabilidad, y se utilizan indicadores financieros para la toma de decisiones. Además, se desarrollan proyecciones, se analizan escenarios de crecimiento y se evalúan inversiones antes de ejecutarlas. Esta capacidad permite que el negocio no solo opere con estabilidad, sino que gestione estratégicamente su expansión. En términos prácticos, la estructura financiera no solo sostiene la operación, sino que impulsa activamente el crecimiento y la sostenibilidad en el largo plazo.""") 

st.write("\nÁrea Técnica:", total_técnica)
if total_técnica <= 22:
    st.write("Nivel PRINCIPIANTE: técnica necesidad")
elif total_técnica <= 41:
    st.write("Nivel INTERMEDIO: técnica oportunidad")
elif total_técnica <= 53:
    st.write("Nivel AVANZADO: técnica funcional")
else:
    st.write("Nivel EXPERTO: técnica estratégica")
if total_técnica <= 22:
    st.write("""En este nivel Principiante, el negocio no cuenta con una estructura técnica definida, lo que provoca que la operación sea inconsistente y dependa en gran medida de una persona clave. La ausencia de procesos técnicos, estándares de calidad y documentación de fallas genera variaciones en el producto o servicio, afectando directamente la experiencia del cliente. Además, la falta de tecnología adecuada, infraestructura suficiente y planeación operativa limita la capacidad de respuesta y crecimiento del negocio. Esta situación incrementa el riesgo de errores operativos, pérdida de clientes y baja eficiencia. En términos prácticos, la operación existe, pero no cuenta con un sistema técnico que le permita garantizar calidad, consistencia ni escalabilidad.""")
elif total_técnica <= 41:
    st.write("""En este nivel Intermedio, el negocio cuenta con ciertos elementos técnicos que le permiten operar, sin embargo, aún no logra mantener consistencia ni control en sus procesos. Existen algunos procedimientos y herramientas, pero no están documentados ni se aplican de manera uniforme, lo que genera variaciones en la calidad del producto o servicio. La operación sigue dependiendo parcialmente de personas clave y las mejoras se realizan de forma reactiva ante los problemas. Además, la infraestructura y la tecnología permiten operar, pero presentan limitaciones para crecer. Esta situación provoca inconsistencias operativas y desgaste del equipo. En términos prácticos, el negocio comienza a estructurar su operación, pero aún no ha consolidado un sistema técnico que garantice estabilidad, calidad y escalabilidad..""")
elif total_técnica <= 53:
   st.write("""En este nivel Avanzado, el negocio ha logrado establecer una estructura técnica funcional que le permite operar con consistencia, calidad y cierto nivel de control. Cuenta con procesos definidos, estándares operativos y una infraestructura que soporta la operación. La calidad del producto o servicio es estable, se utilizan herramientas tecnológicas adecuadas y se identifican y corrigen problemas operativos de manera continua. Además, se aplican mejoras que fortalecen el desempeño del negocio. Sin embargo, aún existe oportunidad de evolucionar hacia un enfoque más estratégico que permita escalar de forma más eficiente. En términos prácticos, el negocio cuenta con una base operativa sólida que le permite sostener su funcionamiento, pero requiere optimización para potenciar su crecimiento.""")
else:
    st.write("""En este nivel Experto, el negocio cuenta con una estructura técnica completamente definida, documentada y optimizada, que le permite operar, escalar y replicar su modelo con eficiencia y control. Los procesos están estandarizados, la calidad es consistente y existen mecanismos claros para la mejora continua. La operación no depende de personas clave, se utilizan tecnologías eficientes y la infraestructura está preparada para soportar el crecimiento. Además, se identifican y eliminan cuellos de botella, y se implementa una planeación operativa estratégica que guía la evolución del negocio. Esta capacidad permite que la operación no solo sostenga la actividad, sino que impulse activamente la expansión. En términos prácticos, el sistema técnico se convierte en un motor de eficiencia, crecimiento y escalabilidad..""")     

st.write("\nÁrea Ecológica:", total_ecológica)
if total_ecológica <= 15:
    st.write("Nivel PRINCIPIANTE: ecológica necesidad")
elif total_ecológica <= 27:
    st.write("Nivel INTERMEDIO: ecológica oportunidad")
elif total_ecológica <= 35:
    st.write("Nivel AVANZADO: ecológica funcional")
else:
    st.write("Nivel EXPERTO: ecológica estratégica")
if total_ecológica <= 15:
    st.write("""En este nivel Principiante, el negocio no cuenta con una estructura que le permita identificar, medir ni gestionar su impacto ambiental, lo que provoca una operación sin conciencia sobre el uso de recursos ni sobre las consecuencias de sus actividades. La ausencia de prácticas de sostenibilidad, el desconocimiento de normativas ambientales y la falta de gestión de residuos generan ineficiencias y riesgos tanto operativos como legales. Además, no se promueve el uso responsable de insumos ni se considera el impacto ecológico en el crecimiento del negocio, lo que limita su capacidad de adaptación a nuevas exigencias del entorno. En términos prácticos, el negocio opera sin integrar la sostenibilidad en su estrategia, lo que afecta su competitividad y lo expone a riesgos reputacionales y regulatorios.""")
elif total_ecológica <= 27:
    st.write("""En este nivel Intermedio, el negocio ha comenzado a reconocer su impacto ambiental y a incorporar algunas prácticas de sostenibilidad, sin embargo, aún no logra gestionarlas de forma consistente ni estructurada. Existen esfuerzos como la reducción parcial de recursos no renovables o ciertas acciones de responsabilidad ambiental, pero estos no se aplican de manera uniforme ni están integrados en la operación diaria. La gestión de residuos y el cumplimiento normativo son incompletos, y la eficiencia energética no es una prioridad constante. Esta falta de continuidad limita el impacto real de las acciones implementadas y genera ineficiencias en el uso de recursos. En términos prácticos, el negocio muestra intención de ser sostenible, pero aún no ha consolidado la sostenibilidad como parte estructural de su operación.""")
elif total_ecológica <= 35:
   st.write("""En este nivel Avanzado, el negocio ha logrado establecer prácticas de sostenibilidad que le permiten gestionar su impacto ambiental con cierto nivel de control y consistencia. Se identifican y monitorean los impactos ambientales, se gestionan residuos de forma adecuada y se promueve el uso responsable de insumos. Además, se cumplen las normativas aplicables y se busca mejorar la eficiencia energética, integrando gradualmente la sostenibilidad dentro de la estrategia del negocio. Sin embargo, aún existe oportunidad de fortalecer su integración estratégica para maximizar su impacto. En términos prácticos, el negocio opera de manera responsable con el entorno, pero requiere evolucionar hacia un enfoque más estratégico que potencie su competitividad y crecimiento.""")
else:
    st.write("""En este nivel Experto, el negocio ha integrado completamente la sostenibilidad como parte central de su estrategia, gestionando y optimizando su impacto ambiental de manera consciente y estructurada. El impacto ambiental está plenamente identificado y medido, se minimiza el uso de recursos no renovables y se implementan prácticas avanzadas que garantizan eficiencia y responsabilidad en la operación. La gestión de residuos es óptima, se cumple y supera la normativa ambiental y se comunica activamente el compromiso sostenible, generando ventajas competitivas. Además, se evalúa el impacto ecológico en cada decisión de crecimiento. En términos prácticos, la sostenibilidad no solo forma parte de la operación, sino que impulsa estratégicamente el posicionamiento, la eficiencia y la permanencia del negocio en el largo plazo.""")   
    
st.write("\nÁrea Legal:", total_legal)
if total_legal <= 30:
    st.write("Nivel PRINCIPIANTE: legal necesidad")
elif total_legal <= 55:
    st.write("Nivel INTERMEDIO: legal oportunidad")
elif total_legal <= 70:
    st.write("Nivel AVANZADO: legal funcional")
else:
    st.write("Nivel EXPERTO: legal estratégica")
if total_legal <= 30:
    st.write("""En este nivel Principiante, el negocio no cuenta con una estructura legal que le permita operar con seguridad jurídica ni cumplir adecuadamente con sus obligaciones fiscales y normativas, lo que lo coloca en una situación de alta vulnerabilidad. La falta de formalización, el incumplimiento en registros, facturación y declaraciones, así como la ausencia de contratos y acuerdos entre socios, generan riesgos constantes tanto operativos como legales. Además, no contar con permisos, asesoría jurídica ni una figura legal alineada a su actividad limita su capacidad de crecimiento y formalización. En términos prácticos, el negocio puede estar operando, pero lo hace en un entorno de alto riesgo que puede derivar en sanciones, conflictos o incluso en la imposibilidad de continuar sus operaciones.""")
elif total_legal <= 55:
    st.write("""EEn este nivel Intermedio, el negocio ha iniciado su proceso de formalización y cuenta con una base legal que le permite operar, sin embargo, aún presenta inconsistencias en el cumplimiento de sus obligaciones fiscales y normativas. Existen avances como el registro ante autoridades, la emisión parcial de facturación y la presencia de algunos contratos, pero estos no se gestionan de forma consistente ni estructurada. La falta de claridad en responsabilidades legales, acuerdos entre socios y el cumplimiento irregular generan riesgos latentes que pueden afectar la estabilidad del negocio. Además, la ausencia de una asesoría legal constante limita la capacidad de anticiparse a problemas. En términos prácticos, el negocio puede operar dentro de un marco legal básico, pero aún no cuenta con una estructura jurídica sólida que garantice control, cumplimiento y crecimiento sostenido.""")
elif total_legal <= 70:
   st.write("""En este nivel Avanzado, el negocio ha logrado establecer una estructura legal funcional que le permite operar con cumplimiento fiscal y normativo, así como con cierto nivel de control y organización. Cuenta con una figura legal adecuada, registros actualizados, emisión de facturación en la mayoría de sus operaciones y cumplimiento regular de sus obligaciones fiscales. Además, dispone de contratos formales con clientes y proveedores, así como acuerdos básicos entre socios que permiten una operación más ordenada. Sin embargo, aún existe oportunidad de evolucionar hacia una gestión legal más estratégica que fortalezca su capacidad de crecimiento. En términos prácticos, el negocio cuenta con una base jurídica sólida para operar, pero requiere optimización para escalar de manera más eficiente y segura.""")
else:
    st.write("""En este nivel Experto, el negocio ha integrado su estructura legal como un componente estratégico que no solo le permite operar con cumplimiento total, sino también crecer, protegerse y consolidarse en el mercado. La figura legal está optimizada, las obligaciones fiscales se cumplen de manera consistente y sin errores, y existen contratos estandarizados que regulan adecuadamente las relaciones con socios, clientes y proveedores. Además, se identifican y gestionan riesgos legales de forma preventiva, se cuenta con asesoría jurídica constante y la estructura legal está diseñada para facilitar la expansión y la atracción de inversión. En términos prácticos, la dimensión legal deja de ser un requisito operativo y se convierte en una herramienta estratégica que impulsa el crecimiento, la estabilidad y la sostenibilidad del negocio en el largo plazo.""")
