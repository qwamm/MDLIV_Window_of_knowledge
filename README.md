# Dyumium
![image](https://github.com/user-attachments/assets/470a6be8-dede-48fe-882e-0994dacc1638)

**Dyumium** - инновационная платформа для взаимодействия с корпоративными базами знаний, направленная на оптимизацию поиска и использования информации в компании. 
Решение снижает временные затраты сотрудников через интеллектуальный интерфейс.
Dyumium – ваш проводник к быстрой адаптации и безупречной точности в управлении корпоративными знаниями.

# VIDEO OF DEMO

# Презентация
[Ссылка на презентацию](https://disk.yandex.ru/d/5g5WhO0DWjqa7w)

# Наша система
![image](https://github.com/user-attachments/assets/e5e5b92b-93df-4ff7-987b-0980f06e0901)

# Технологическое описание процесса работы системы
![image](https://github.com/user-attachments/assets/f30ee946-260c-4be0-a843-e38c4659a04c)

**01. Этап ETL**

Данные из базы знаний извлекаются и проходят предварительную обработку. Информация структурируется и подготавливается для дальнейшей векторизации, чтобы обеспечить корректность и точность поиска.

**02. Векторизация данных**

Каждый текстовый блок преобразуется в вектор фиксированной размерности. Этот процесс выполняется с помощью мощной языковой модели (LLM), которая сохраняет семантическую связь между словами и контекстом.

**03. API-обработка**

Пользовательский запрос поступает в систему через API. Запрос, как и исходные данные, преобразуется в векторное представление, что позволяет анализировать его смысл, а не только ключевые слова.
  
**04. Поиск данных**

Сравнение вектора запроса с хранимыми векторами выполняется через Qdrant. Используются метрики схожести, такие как косинусное расстояние, для определения наиболее релевантных текстов.

**05. Формирование ответа**

На основе результатов поиска система извлекает релевантные блоки информации, анализирует их и формирует понятный для пользователя ответ.

**06. Результат**

Мы создали эффективное решение, которое использует векторные представления данных и интеграцию с **Qdrant** – мощным хранилищем векторов. Это обеспечивает:

- **Молниеносный поиск:** быстрый доступ к нужной информации.
- **Высокую точность:** понимание смысла запросов, а не просто совпадение слов.
- **Масштабируемость:** возможность работать с большими объемами данных без потери производительности.

Наше решение превращает сложные запросы в простые и точные ответы, создавая новый уровень взаимодействия с базами знаний.

# Модели
## Администратор
Сотрудник компании регистрируется на портале. 

# Методы API
Для отладки и тестирования всего функционала можно заходить на http://127.0.0.1:8080/api/docs, где в доступной форме можно посылать запросы на сервер и получать ответы.
![image](https://github.com/user-attachments/assets/d11046a3-bc45-4893-bf31-622787ce2c3f)
![image](https://github.com/user-attachments/assets/40616fcf-e50b-4663-8fa3-362949705c89)

# Используемые технологии
## FastAPI
![image](https://github.com/user-attachments/assets/f7aa8ae6-6a7b-4471-977f-ef945cfc0351)
> Для Бэкенда: потому что fast и потому что API.
## SQLalchemy
![image](https://github.com/user-attachments/assets/b4e9d20f-bbd1-4dc0-a4d7-acd338336899)
> Для работы с базой данных
## React
![image](https://github.com/user-attachments/assets/4802e201-6426-41ad-97d1-53838534d34a)
> Для фронтенда
## Qdrant
![image](https://github.com/user-attachments/assets/02218a2a-c3bb-4e1e-9122-7fc8b6f60388)
> Для векторизации текста из документов
## Llama cpp
![image](https://github.com/user-attachments/assets/3e96dc20-e064-4572-ad1b-93a4a638191d)
> Для работы с LLM
## qwen2-0_5b-instruct-q5_k_m
![image](https://github.com/user-attachments/assets/3f4bde79-bfed-40c4-8d48-339f6fc828b6)
> Модель, участвующая в цикле RAG

