print("DIAGNÓSTICO EMPRESARIAL - ÁREA ADMINISTRATIVA/ORGANIZACIONAL")
print("Este cuestionario tiene como objetivo evaluar el nivel de madurez de un emprendimiento en seis áreas clave: legal, administrativa, comercial, financiera, técnica y ecológica.No existen respuestas correctas o incorrectas. Responde con honestidad para obtener un diagnóstico útil.")
print("Escala: 1 = No existe, 2 = Existe de manera informal, 3 = Existe parcialmente, 4 = Existe y funciona adecuadamente, 5 = Existe y está documentado\n")

total_admin = 0

total_admin += int(input("1. ¿Cuenta con estructura organizacional definida?: "))
total_admin += int(input("2. ¿Están claros los roles y responsabilidades?: "))
total_admin += int(input("3. ¿Existe un responsable de decisiones clave?: "))
total_admin += int(input("4. ¿Los socios tienen funciones diferenciadas?: "))
total_admin += int(input("5. ¿Las decisiones se documentan?: "))
total_admin += int(input("6. ¿Existen procesos definidos para actividades clave?: "))
total_admin += int(input("7. ¿Los procesos están documentados?: "))
total_admin += int(input("8. ¿Se usan herramientas de seguimiento de tareas?: "))
total_admin += int(input("9. ¿Se mide el desempeño periódicamente?: "))
total_admin += int(input("10. ¿Existen indicadores administrativos?: "))
total_admin += int(input("11. ¿Tiene objetivos claros a corto y mediano plazo?: "))
total_admin += int(input("12. ¿Realiza planeación anual o semestral?: "))
total_admin += int(input("13. ¿Revisa resultados contra lo planeado?: "))
total_admin += int(input("14. ¿Ajusta estrategias cuando algo no funciona?: "))
total_admin += int(input("15. ¿El negocio depende de una sola persona?: "))
total_admin += int(input("16. ¿Cuenta con personal formal?: "))
total_admin += int(input("17. ¿Hay claridad en horarios y pagos?: "))
total_admin += int(input("18. ¿Se capacita al personal regularmente?: "))
total_admin += int(input("19. ¿Existe alta rotación de personal?: "))
total_admin += int(input("20. ¿El clima organizacional es favorable?: "))

print("\nPuntaje total área administrativa:", total_admin)

if total_admin <= 30:
    print("Nivel PRINCIPIANTE: estructura necesidad")
elif total_admin <= 55:
    print("Nivel INTERMEDIO: estructura oportunidad")
elif total_admin <= 70:
    print("Nivel AVANZADO: estructura funcional")
else:
    print("Nivel EXPERTO: estructura estratégico")
    
print("\nDIAGNÓSTICO EMPRESARIAL - ÁREA COMERCIAL")
print("Escala: 1 = No existe, 2 = Informal, 3 = Parcial, 4 = Funciona, 5 = Documentado\n")

total_comercial = 0

total_comercial += int(input("21. ¿Tiene definida su propuesta de valor?: "))
total_comercial += int(input("22. ¿Resuelve un problema real del cliente?: "))
total_comercial += int(input("23. ¿Tiene identificado a su cliente objetivo?: "))
total_comercial += int(input("24. ¿Conoce el perfil del cliente ideal?: "))
total_comercial += int(input("25. ¿Se diferencia de la competencia?: "))
total_comercial += int(input("26. ¿Cuenta con canales de venta definidos?: "))
total_comercial += int(input("27. ¿Los canales actuales son efectivos?: "))
total_comercial += int(input("28. ¿Existe un proceso de ventas estructurado?: "))
total_comercial += int(input("29. ¿Mide la conversión de prospectos?: "))
total_comercial += int(input("30. ¿Da seguimiento a clientes potenciales?: "))
total_comercial += int(input("31. ¿El modelo de ingresos está definido?: "))
total_comercial += int(input("32. ¿Los precios cubren costos y generan utilidad?: "))
total_comercial += int(input("33. ¿Revisa precios periódicamente?: "))
total_comercial += int(input("34. ¿Depende de pocos clientes?: "))
total_comercial += int(input("35. ¿Los ingresos son recurrentes?: "))
total_comercial += int(input("36. ¿Realiza acciones de marketing constantes?: "))
total_comercial += int(input("37. ¿Utiliza medios digitales para vender?: "))
total_comercial += int(input("38. ¿Mide la satisfacción del cliente?: "))
total_comercial += int(input("39. ¿Cuenta con estrategias de fidelización?: "))
total_comercial += int(input("40. ¿La marca es reconocible en su mercado?: "))

print("\nPuntaje total área comercial:", total_comercial)

if total_comercial <= 30:
    print("Nivel PRINCIPIANTE: comercial necesidad")
elif total_comercial <= 55:
    print("Nivel INTERMEDIO: comercial oportunidad")
elif total_comercial <= 70:
    print("Nivel AVANZADO: comercial funcional")
else:
    print("Nivel EXPERTO: comercial estratégica")
    
print("\nDIAGNÓSTICO EMPRESARIAL - ÁREA FINANCIERA")
print("Escala: 1 = No existe, 2 = Informal, 3 = Parcial, 4 = Funciona, 5 = Documentado\n")

total_financiera = 0

total_financiera += int(input("41. ¿Lleva registros financieros formales?: "))
total_financiera += int(input("42. ¿Elabora estados financieros periódicos?: "))
total_financiera += int(input("43. ¿Separa finanzas personales y del negocio?: "))
total_financiera += int(input("44. ¿Conoce su flujo de efectivo mensual?: "))
total_financiera += int(input("45. ¿Identifica ingresos y egresos claramente?: "))
total_financiera += int(input("46. ¿El negocio es rentable actualmente?: "))
total_financiera += int(input("47. ¿Conoce sus costos fijos y variables?: "))
total_financiera += int(input("48. ¿Calcula su punto de equilibrio?: "))
total_financiera += int(input("49. ¿Analiza márgenes de utilidad?: "))
total_financiera += int(input("50. ¿Identifica fugas de dinero?: "))
total_financiera += int(input("51. ¿Cuenta con liquidez suficiente?: "))
total_financiera += int(input("52. ¿Ha utilizado financiamiento externo?: "))
total_financiera += int(input("53. ¿Las deudas son manejables?: "))
total_financiera += int(input("54. ¿Conoce el costo de su financiamiento?: "))
total_financiera += int(input("55. ¿Tiene planeación para contingencias?: "))
total_financiera += int(input("56. ¿Cuenta con proyecciones financieras?: "))
total_financiera += int(input("57. ¿Analiza escenarios de crecimiento?: "))
total_financiera += int(input("58. ¿Reinvierte utilidades en el negocio?: "))
total_financiera += int(input("59. ¿Evalúa inversiones antes de ejecutarlas?: "))
total_financiera += int(input("60. ¿Puede crecer sin comprometer estabilidad financiera?: "))

print("\nPuntaje total área financiera:", total_financiera)

if total_financiera <= 30:
    print("Nivel PRINCIPIANTE: financiera necesidad")
elif total_financiera <= 55:
    print("Nivel INTERMEDIO: financiera oportunidad")
elif total_financiera <= 70:
    print("Nivel AVANZADO: financiera funcional")
else:
    print("Nivel EXPERTO: financiera estratégica")

print("\nDIAGNÓSTICO EMPRESARIAL - ÁREA TÉCNICA")
print("Escala: 1 = No existe, 2 = Informal, 3 = Parcial, 4 = Funciona, 5 = Documentado\n")

total_técnica = 0

total_técnica += int(input("61. ¿Domina técnicamente su producto o servicio?: "))
total_técnica += int(input("62. ¿Tiene procesos técnicos definidos?: "))
total_técnica += int(input("63. ¿La calidad es consistente?: "))
total_técnica += int(input("64. ¿Cuenta con estándares de calidad?: "))
total_técnica += int(input("65. ¿La operación depende de una persona clave?: "))
total_técnica += int(input("66. ¿Utiliza tecnología adecuada?: "))
total_técnica += int(input("67. ¿La infraestructura es suficiente?: "))
total_técnica += int(input("68. ¿Existen cuellos de botella operativos?: "))
total_técnica += int(input("69. ¿La operación es escalable?: "))
total_técnica += int(input("70. ¿Aplica mejoras continuas?: "))
total_técnica += int(input("71. ¿Documenta fallas operativas?: "))
total_técnica += int(input("72. ¿Aplica acciones correctivas?: "))
total_técnica += int(input("73. ¿La capacidad instalada cubre la demanda?: "))
total_técnica += int(input("74. ¿Planea la operación a futuro?: "))
total_técnica += int(input("75. ¿La operación es replicable?: "))

print("\nPuntaje total área técnica/operativa:", total_técnica)

if total_técnica <= 22:
    print("Nivel PRINCIPIANTE: técnica necesidad")
elif total_técnica <= 41:
    print("Nivel INTERMEDIO: técnica oportunidad")
elif total_técnica <= 53:
    print("Nivel AVANZADO: técnica funcional")
else:
    print("Nivel EXPERTO: técnica estratégica")

print("\nDIAGNÓSTICO EMPRESARIAL - ÁREA ECOLÓGICA")
print("Escala: 1 = No existe, 2 = Informal, 3 = Parcial, 4 = Funciona, 5 = Documentado\n")

total_ecológica = 0

total_ecológica += int(input("76. ¿Identifica su impacto ambiental?: "))
total_ecológica += int(input("77. ¿Minimiza el uso de recursos no renovables?: "))
total_ecológica += int(input("78. ¿Gestiona adecuadamente sus residuos?: "))
total_ecológica += int(input("79. ¿Promueve el uso responsable de insumos?: "))
total_ecológica += int(input("80. ¿Cumple normativas ambientales aplicables?: "))
total_ecológica += int(input("81. ¿Aplica prácticas de sostenibilidad?: "))
total_ecológica += int(input("82. ¿Comunica su compromiso ambiental?: "))
total_ecológica += int(input("83. ¿Busca eficiencia energética?: "))
total_ecológica += int(input("84. ¿Evalúa impacto ecológico al crecer?: "))
total_ecológica += int(input("85. ¿La sostenibilidad es parte de su estrategia?: "))

print("\nPuntaje total área ecológica:", total_ecológica)

if total_ecológica <= 15:
    print("Nivel PRINCIPIANTE: ecológica necesidad")
elif total_ecológica <= 27:
    print("Nivel INTERMEDIO: ecológica oportunidad")
elif total_ecológica <= 35:
    print("Nivel AVANZADO: ecológica funcional")
else:
    print("Nivel EXPERTO: ecológica estratégica")

print("\nDIAGNÓSTICO EMPRESARIAL - ÁREA LEGAL")
print("Escala: 1 = No existe, 2 = Informal, 3 = Parcial, 4 = Funciona, 5 = Documentado\n")

total_legal = 0

total_legal += int(input("786. ¿El negocio está legalmente constituido?: "))
total_legal += int(input("87. ¿Opera como persona física o moral acorde a su actividad?: "))
total_legal += int(input("88. ¿La figura legal es congruente con el giro del negocio?: "))
total_legal += int(input("89. ¿Cuenta con acta constitutiva vigente (si aplica)?: "))
total_legal += int(input("90. ¿Los socios están correctamente registrados?: "))
total_legal += int(input("91. ¿Está dado de alta ante el SAT?: "))
total_legal += int(input("92. ¿El régimen fiscal corresponde a su actividad real?: "))
total_legal += int(input("93. ¿Emite facturas por todos sus ingresos?: "))
total_legal += int(input("94. ¿Presenta declaraciones fiscales en tiempo y forma?: "))
total_legal += int(input("95. ¿Tiene adeudos fiscales pendientes?: "))
total_legal += int(input("96. ¿Cuenta con contratos formales con proveedores?: "))
total_legal += int(input("97. ¿Cuenta con contratos con clientes cuando es necesario?: "))
total_legal += int(input("98. ¿Existen convenios o acuerdos entre socios?: "))
total_legal += int(input("99. ¿Están definidas las responsabilidades legales de cada socio?: "))
total_legal += int(input("100. ¿Existen cláusulas de salida o disolución?: "))
total_legal += int(input("101. ¿Cuenta con licencias o permisos para operar?: "))
total_legal += int(input("102. ¿Cumple con normativas aplicables?: "))
total_legal += int(input("103. ¿Tiene identificados riesgos legales actuales?: "))
total_legal += int(input("104. ¿Cuenta con asesoría legal de respaldo?: "))
total_legal += int(input("105. ¿La estructura legal permite el crecimiento del negocio?: "))

print("\nPuntaje total área legal:", total_legal)

if total_legal <= 30:
    print("Nivel PRINCIPIANTE: legal necesidad")
elif total_legal <= 55:
    print("Nivel INTERMEDIO: legal oportunidad")
elif total_legal <= 70:
    print("Nivel AVANZADO: legal funcional")
else:
    print("Nivel EXPERTO: legal estratégica")

print("\nDIAGNÓSTICO EMPRESARIAL - RESUMEN")

print("\nÁrea Administrativa:", total_admin)
if total_admin <= 30:
    print("Nivel PRINCIPIANTE: estructura necesidad")
elif total_admin <= 55:
    print("Nivel INTERMEDIO: estructura oportunidad")
elif total_admin <= 70:
    print("Nivel AVANZADO: estructura funcional")
else:
    print("Nivel EXPERTO: estructura estratégico")
if total_admin <= 30:
    print("""En este nivel Principiante, el negocio opera sin una estructura organizacional clara, lo que implica que las decisiones, los procesos y las responsabilidades no están formalmene definidos y dependen en gran medida de una sola persona. La ausencia de procesos documentados, indicadores y planeación provoca que la operación funcione más por esfuerzo personal que por un sistema establecido, generando desorden y limitando la capacidad de crecimiento. Esta situación representa un alto riesgo operativo, ya que dificulta la delegación, incrementa la carga del dueño y puede derivar en ineficiencias constantes. En términos prácticos, el negocio sí existe y opera, pero aún no cuenta con una base organizacional sólida que le permita sostenerse y evolucionar de manera estructurada.""")
elif total_admin <= 55:
    print("""En este nivel Intermedio, el negocio cuenta con ciertos elementos de estructura que le permiten operar, sin embargo, aún no logra mantener un control consistente sobre sus procesos y resultados. Existen avances como la definición parcial de roles, algunos procesos en marcha y ciertos intentos de medición, pero estos no están documentados ni se aplican de manera uniforme. La planeación puede estar presente, aunque no siempre se sigue, y los ajustes suelen realizarse de forma reactiva ante los problemas. Esta situación genera un crecimiento desordenado, desgaste operativo e inconsistencias en los resultados. En términos prácticos, el negocio muestra intención de organización, pero aún no ha consolidado una estructura que le permita operar con estabilidad y control.""")
elif total_admin <= 70:
   print("""En este nivel Avanzado, el negocio ha logrado establecer una estructura funcional que le permite operar con orden y cierto grado de control. Cuenta con procesos definidos y en uso, roles claros en la mayoría del equipo, así como indicadores que permiten dar seguimiento a su desempeño. La planeación se realiza de forma periódica y existe un seguimiento operativo constante que favorece la estabilidad del negocio. Esto indica que la operación ya no depende únicamente del esfuerzo individual, sino de un sistema organizado. Sin embargo, existe el riesgo de estancamiento si no se continúa evolucionando y optimizando. En términos prácticos, el negocio funciona adecuadamente y cuenta con bases sólidas, pero requiere avanzar hacia un enfoque más estratégico para seguir creciendo.""")
else:
    print("""En este nivel Experto, el negocio cuenta con una estructura organizacional completamente definida que le permite no solo operar, sino también escalar y sostener su crecimiento. Los procesos están documentados y son replicables, los indicadores son claros y se utilizan activamente para la toma de decisiones, y existe una planeación estratégica que guía el rumbo del negocio. Además, se observa una cultura organizacional estable que facilita la delegación y el desarrollo del equipo. Esta estructura convierte al negocio en un sistema preparado para expandirse de manera ordenada. No obstante, implica el reto de gestionar una mayor complejidad y mantener una evolución constante. En términos prácticos, la organización no solo sostiene la operación, sino que impulsa activamente su crecimiento y posicionamiento.""")

print("\nÁrea Comercial:", total_comercial)
if total_comercial <= 30:
    print("Nivel PRINCIPIANTE: comercial necesidad")
elif total_comercial <= 55:
    print("Nivel INTERMEDIO: comercial oportunidad")
elif total_comercial <= 70:
    print("Nivel AVANZADO: comercial funcional")
else:
    print("Nivel EXPERTO: comercial estratégica")
if total_comercial <= 30:
    print("""En este nivel Principiante, el negocio no cuenta con una estructura comercial definida, lo que implica que la propuesta de valor, el cliente objetivo y los canales de venta no están claramente establecidos. La generación de ingresos depende de esfuerzos aislados y no de un proceso de ventas estructurado, lo que provoca resultados inconsistentes y poco predecibles. La ausencia de estrategias de marketing, seguimiento a clientes y medición de resultados limita la capacidad de crecimiento. Esta situación representa un alto riesgo comercial, ya que dificulta la generación de ingresos estables y sostenibles. En términos prácticos, el negocio puede vender en ciertos momentos, pero aún no cuenta con un sistema comercial sólido que le permita sostener y escalar sus ingresos de manera estructurada.""")
elif total_comercial <= 55:
    print("""En este nivel Intermedio, el negocio cuenta con ciertos elementos comerciales que le permiten generar ingresos, sin embargo, aún no logra mantener un control consistente sobre su proceso de ventas y sus resultados. Existen avances como una propuesta de valor básica, algunos canales de venta activos y cierto conocimiento del cliente, pero estos elementos no están completamente definidos ni operan de manera uniforme. Las acciones de marketing y el seguimiento a clientes suelen ser irregulares, lo que provoca ingresos variables y dificulta la estabilidad del negocio. Esta situación representa un riesgo comercial, ya que limita el aprovechamiento de oportunidades y el crecimiento sostenido. En términos prácticos, el negocio tiene capacidad de vender, pero aún no ha consolidado un sistema comercial estructurado que le permita generar ingresos de manera constante y predecible.""")
elif total_comercial <= 70:
   print("""En este nivel Avanzado, el negocio ha logrado estructurar un sistema comercial funcional que le permite generar ingresos de manera constante y con cierto nivel de control. Cuenta con una propuesta de valor clara, identifica a su cliente objetivo y utiliza canales de venta definidos que contribuyen a la generación de resultados. Además, existe un proceso de ventas establecido, se da seguimiento a clientes potenciales y se implementan acciones de marketing de forma regular. Esto permite que los ingresos sean más estables y predecibles. Sin embargo, aún existe oportunidad de optimizar y escalar el sistema comercial. En términos prácticos, el negocio vende de manera consistente, pero requiere evolucionar hacia un enfoque más estratégico para potenciar su crecimiento.""")
else:
    print("""En este nivel Experto, el negocio cuenta con una estructura comercial sólida, optimizada y orientada estratégicamente al crecimiento. La propuesta de valor está claramente posicionada, el cliente ideal se encuentra bien definido y segmentado, y los canales de venta son efectivos y escalables. El proceso comercial se encuentra estructurado y medido, permitiendo analizar la conversión de prospectos, dar seguimiento sistemático a clientes y aplicar estrategias de fidelización. Además, se mide la satisfacción del cliente y los ingresos son recurrentes y sostenibles. Esta capacidad permite que el negocio no solo genere ventas, sino que gestione estratégicamente su crecimiento en el mercado. En términos prácticos, el sistema comercial no solo sostiene la operación, sino que impulsa activamente la expansión y posicionamiento del negocio.""") 

print("\nÁrea Financiera:", total_financiera)
if total_financiera <= 30:
    print("Nivel PRINCIPIANTE: financiera necesidad")
elif total_financiera <= 55:
    print("Nivel INTERMEDIO: financiera oportunidad")
elif total_financiera <= 70:
    print("Nivel AVANZADO: financiera funcional")
else:
    print("Nivel EXPERTO: financiera estratégica")
if total_financiera <= 30:
    print("""En este nivel Principiante, el negocio no cuenta con una estructura financiera definida, lo que implica que no tiene claridad sobre su flujo de efectivo, sus costos ni su rentabilidad. La ausencia de registros financieros formales y de estados financieros periódicos impide tener visibilidad sobre su situación económica, mientras que la mezcla entre finanzas personales y del negocio genera desorden en el uso de los recursos. Esta falta de control limita la toma de decisiones y aumenta el riesgo de pérdidas no detectadas y problemas de liquidez. En términos prácticos, el negocio puede generar ingresos, pero no cuenta con una base financiera que le permita entender su desempeño ni sostener su operación de manera estructurada.""")
elif total_financiera <= 55:
    print("""En este nivel Intermedio, el negocio cuenta con ciertos elementos financieros que le permiten tener una visión parcial de su situación, sin embargo, aún no logra mantener un control consistente sobre sus recursos ni sobre sus resultados. Existen algunos registros y reportes, pero no están completos ni actualizados, y el análisis financiero se realiza de manera irregular. La separación entre finanzas personales y del negocio es parcial, lo que genera desorden en la administración del dinero. Esta falta de consistencia limita la toma de decisiones y aumenta el riesgo de errores financieros y problemas de liquidez. En términos prácticos, el negocio comienza a entender sus finanzas, pero aún no ha consolidado un sistema que le permita controlarlas y utilizarlas de forma estratégica.""")
elif total_financiera <= 70:
   print("""En este nivel Avanzado, el negocio ha logrado establecer una estructura financiera funcional que le permite operar con control y tomar decisiones con base en información confiable. Cuenta con registros financieros formales, estados financieros periódicos y una clara separación entre las finanzas personales y las del negocio. Se monitorea el flujo de efectivo, se identifican costos y márgenes, y se realizan análisis que favorecen la estabilidad operativa. Sin embargo, aún existe oportunidad de optimizar y evolucionar hacia un enfoque más estratégico. En términos prácticos, el negocio cuenta con bases financieras sólidas que le permiten sostener su operación, pero requiere fortalecer su análisis y planeación para impulsar su crecimiento.""")
else:
    print("""En este nivel Experto, el negocio cuenta con una estructura financiera sólida, completa y orientada estratégicamente al crecimiento. Los registros son precisos y actualizados, los estados financieros se analizan de forma periódica y existe un control total del flujo de efectivo. Se optimizan costos, márgenes y rentabilidad, y se utilizan indicadores financieros para la toma de decisiones. Además, se desarrollan proyecciones, se analizan escenarios de crecimiento y se evalúan inversiones antes de ejecutarlas. Esta capacidad permite que el negocio no solo opere con estabilidad, sino que gestione estratégicamente su expansión. En términos prácticos, la estructura financiera no solo sostiene la operación, sino que impulsa activamente el crecimiento y la sostenibilidad en el largo plazo.""") 

print("\nÁrea Técnica:", total_técnica)
if total_técnica <= 22:
    print("Nivel PRINCIPIANTE: técnica necesidad")
elif total_técnica <= 41:
    print("Nivel INTERMEDIO: técnica oportunidad")
elif total_técnica <= 53:
    print("Nivel AVANZADO: técnica funcional")
else:
    print("Nivel EXPERTO: técnica estratégica")
if total_técnica <= 22:
    print("""En este nivel Principiante, el negocio no cuenta con una estructura técnica definida, lo que provoca que la operación sea inconsistente y dependa en gran medida de una persona clave. La ausencia de procesos técnicos, estándares de calidad y documentación de fallas genera variaciones en el producto o servicio, afectando directamente la experiencia del cliente. Además, la falta de tecnología adecuada, infraestructura suficiente y planeación operativa limita la capacidad de respuesta y crecimiento del negocio. Esta situación incrementa el riesgo de errores operativos, pérdida de clientes y baja eficiencia. En términos prácticos, la operación existe, pero no cuenta con un sistema técnico que le permita garantizar calidad, consistencia ni escalabilidad.""")
elif total_técnica <= 41:
    print("""En este nivel Intermedio, el negocio cuenta con ciertos elementos técnicos que le permiten operar, sin embargo, aún no logra mantener consistencia ni control en sus procesos. Existen algunos procedimientos y herramientas, pero no están documentados ni se aplican de manera uniforme, lo que genera variaciones en la calidad del producto o servicio. La operación sigue dependiendo parcialmente de personas clave y las mejoras se realizan de forma reactiva ante los problemas. Además, la infraestructura y la tecnología permiten operar, pero presentan limitaciones para crecer. Esta situación provoca inconsistencias operativas y desgaste del equipo. En términos prácticos, el negocio comienza a estructurar su operación, pero aún no ha consolidado un sistema técnico que garantice estabilidad, calidad y escalabilidad..""")
elif total_técnica <= 53:
   print("""En este nivel Avanzado, el negocio ha logrado establecer una estructura técnica funcional que le permite operar con consistencia, calidad y cierto nivel de control. Cuenta con procesos definidos, estándares operativos y una infraestructura que soporta la operación. La calidad del producto o servicio es estable, se utilizan herramientas tecnológicas adecuadas y se identifican y corrigen problemas operativos de manera continua. Además, se aplican mejoras que fortalecen el desempeño del negocio. Sin embargo, aún existe oportunidad de evolucionar hacia un enfoque más estratégico que permita escalar de forma más eficiente. En términos prácticos, el negocio cuenta con una base operativa sólida que le permite sostener su funcionamiento, pero requiere optimización para potenciar su crecimiento.""")
else:
    print("""En este nivel Experto, el negocio cuenta con una estructura técnica completamente definida, documentada y optimizada, que le permite operar, escalar y replicar su modelo con eficiencia y control. Los procesos están estandarizados, la calidad es consistente y existen mecanismos claros para la mejora continua. La operación no depende de personas clave, se utilizan tecnologías eficientes y la infraestructura está preparada para soportar el crecimiento. Además, se identifican y eliminan cuellos de botella, y se implementa una planeación operativa estratégica que guía la evolución del negocio. Esta capacidad permite que la operación no solo sostenga la actividad, sino que impulse activamente la expansión. En términos prácticos, el sistema técnico se convierte en un motor de eficiencia, crecimiento y escalabilidad..""")     

print("\nÁrea Ecológica:", total_ecológica)
if total_ecológica <= 15:
    print("Nivel PRINCIPIANTE: ecológica necesidad")
elif total_ecológica <= 27:
    print("Nivel INTERMEDIO: ecológica oportunidad")
elif total_ecológica <= 35:
    print("Nivel AVANZADO: ecológica funcional")
else:
    print("Nivel EXPERTO: ecológica estratégica")
if total_ecológica <= 15:
    print("""En este nivel Principiante, el negocio no cuenta con una estructura que le permita identificar, medir ni gestionar su impacto ambiental, lo que provoca una operación sin conciencia sobre el uso de recursos ni sobre las consecuencias de sus actividades. La ausencia de prácticas de sostenibilidad, el desconocimiento de normativas ambientales y la falta de gestión de residuos generan ineficiencias y riesgos tanto operativos como legales. Además, no se promueve el uso responsable de insumos ni se considera el impacto ecológico en el crecimiento del negocio, lo que limita su capacidad de adaptación a nuevas exigencias del entorno. En términos prácticos, el negocio opera sin integrar la sostenibilidad en su estrategia, lo que afecta su competitividad y lo expone a riesgos reputacionales y regulatorios.""")
elif total_ecológica <= 27:
    print("""En este nivel Intermedio, el negocio ha comenzado a reconocer su impacto ambiental y a incorporar algunas prácticas de sostenibilidad, sin embargo, aún no logra gestionarlas de forma consistente ni estructurada. Existen esfuerzos como la reducción parcial de recursos no renovables o ciertas acciones de responsabilidad ambiental, pero estos no se aplican de manera uniforme ni están integrados en la operación diaria. La gestión de residuos y el cumplimiento normativo son incompletos, y la eficiencia energética no es una prioridad constante. Esta falta de continuidad limita el impacto real de las acciones implementadas y genera ineficiencias en el uso de recursos. En términos prácticos, el negocio muestra intención de ser sostenible, pero aún no ha consolidado la sostenibilidad como parte estructural de su operación.""")
elif total_ecológica <= 35:
   print("""En este nivel Avanzado, el negocio ha logrado establecer prácticas de sostenibilidad que le permiten gestionar su impacto ambiental con cierto nivel de control y consistencia. Se identifican y monitorean los impactos ambientales, se gestionan residuos de forma adecuada y se promueve el uso responsable de insumos. Además, se cumplen las normativas aplicables y se busca mejorar la eficiencia energética, integrando gradualmente la sostenibilidad dentro de la estrategia del negocio. Sin embargo, aún existe oportunidad de fortalecer su integración estratégica para maximizar su impacto. En términos prácticos, el negocio opera de manera responsable con el entorno, pero requiere evolucionar hacia un enfoque más estratégico que potencie su competitividad y crecimiento.""")
else:
    print("""En este nivel Experto, el negocio ha integrado completamente la sostenibilidad como parte central de su estrategia, gestionando y optimizando su impacto ambiental de manera consciente y estructurada. El impacto ambiental está plenamente identificado y medido, se minimiza el uso de recursos no renovables y se implementan prácticas avanzadas que garantizan eficiencia y responsabilidad en la operación. La gestión de residuos es óptima, se cumple y supera la normativa ambiental y se comunica activamente el compromiso sostenible, generando ventajas competitivas. Además, se evalúa el impacto ecológico en cada decisión de crecimiento. En términos prácticos, la sostenibilidad no solo forma parte de la operación, sino que impulsa estratégicamente el posicionamiento, la eficiencia y la permanencia del negocio en el largo plazo.""")   
    
print("\nÁrea Legal:", total_legal)
if total_legal <= 30:
    print("Nivel PRINCIPIANTE: legal necesidad")
elif total_legal <= 55:
    print("Nivel INTERMEDIO: legal oportunidad")
elif total_legal <= 70:
    print("Nivel AVANZADO: legal funcional")
else:
    print("Nivel EXPERTO: legal estratégica")
if total_legal <= 30:
    print("""En este nivel Principiante, el negocio no cuenta con una estructura legal que le permita operar con seguridad jurídica ni cumplir adecuadamente con sus obligaciones fiscales y normativas, lo que lo coloca en una situación de alta vulnerabilidad. La falta de formalización, el incumplimiento en registros, facturación y declaraciones, así como la ausencia de contratos y acuerdos entre socios, generan riesgos constantes tanto operativos como legales. Además, no contar con permisos, asesoría jurídica ni una figura legal alineada a su actividad limita su capacidad de crecimiento y formalización. En términos prácticos, el negocio puede estar operando, pero lo hace en un entorno de alto riesgo que puede derivar en sanciones, conflictos o incluso en la imposibilidad de continuar sus operaciones.""")
elif total_legal <= 55:
    print("""EEn este nivel Intermedio, el negocio ha iniciado su proceso de formalización y cuenta con una base legal que le permite operar, sin embargo, aún presenta inconsistencias en el cumplimiento de sus obligaciones fiscales y normativas. Existen avances como el registro ante autoridades, la emisión parcial de facturación y la presencia de algunos contratos, pero estos no se gestionan de forma consistente ni estructurada. La falta de claridad en responsabilidades legales, acuerdos entre socios y el cumplimiento irregular generan riesgos latentes que pueden afectar la estabilidad del negocio. Además, la ausencia de una asesoría legal constante limita la capacidad de anticiparse a problemas. En términos prácticos, el negocio puede operar dentro de un marco legal básico, pero aún no cuenta con una estructura jurídica sólida que garantice control, cumplimiento y crecimiento sostenido.""")
elif total_legal <= 70:
   print("""En este nivel Avanzado, el negocio ha logrado establecer una estructura legal funcional que le permite operar con cumplimiento fiscal y normativo, así como con cierto nivel de control y organización. Cuenta con una figura legal adecuada, registros actualizados, emisión de facturación en la mayoría de sus operaciones y cumplimiento regular de sus obligaciones fiscales. Además, dispone de contratos formales con clientes y proveedores, así como acuerdos básicos entre socios que permiten una operación más ordenada. Sin embargo, aún existe oportunidad de evolucionar hacia una gestión legal más estratégica que fortalezca su capacidad de crecimiento. En términos prácticos, el negocio cuenta con una base jurídica sólida para operar, pero requiere optimización para escalar de manera más eficiente y segura.""")
else:
    print("""En este nivel Experto, el negocio ha integrado su estructura legal como un componente estratégico que no solo le permite operar con cumplimiento total, sino también crecer, protegerse y consolidarse en el mercado. La figura legal está optimizada, las obligaciones fiscales se cumplen de manera consistente y sin errores, y existen contratos estandarizados que regulan adecuadamente las relaciones con socios, clientes y proveedores. Además, se identifican y gestionan riesgos legales de forma preventiva, se cuenta con asesoría jurídica constante y la estructura legal está diseñada para facilitar la expansión y la atracción de inversión. En términos prácticos, la dimensión legal deja de ser un requisito operativo y se convierte en una herramienta estratégica que impulsa el crecimiento, la estabilidad y la sostenibilidad del negocio en el largo plazo.""") 
