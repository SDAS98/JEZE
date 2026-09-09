# JEZE — Audio Social Network 🎙️

> **Red social y plataforma de comunicación basada en audio, diseñada con un modelo híbrido (Asíncrono + En Vivo) y enfoque prioritario en accesibilidad universal para personas con discapacidad visual o baja visión.**

---

## 📋 Tabla de Contenidos
- [1. Visión y Descripción](#1-visión-y-descripción)
- [2. Enfoque Híbrido](#2-enfoque-híbrido)
- [3. Requisitos de Accesibilidad (A11y)](#3-requisitos-de-accesibilidad-a11y)
- [4. Características Clave (MVP)](#4-características-clave-mvp)
- [5. Arquitectura Técnica](#5-arquitectura-técnica)
- [6. Estructura del Repositorio](#6-estructura-del-repositorio)
- [7. Hoja de Ruta (Roadmap)](#7-hoja-de-ruta-roadmap)

---

## 1. Visión y Descripción

<<<<<<< HEAD
**JEZE** nace para transformar la manera en que nos comunicamos en línea, sustituyendo el texto y las pantallas sobrecargadas por el poder de la voz humana. 

A diferencia de las plataformas tradicionales de podcasts o redes sociales visuales, JEZE está enfocada en la **comunicación conversacional fluida**. Ha sido concebida bajo el principio de **"Accesibilidad Primero" (Accessibility-First)**, garantizando que usuarios ciegos o con visión reducida disfruten de una experiencia nativa, ágil y autónoma, sin barreras de interfaz.
=======
**VocaLink** nace para transformar la manera en que nos comunicamos en línea, sustituyendo el texto y las pantallas sobrecargadas por el poder de la voz humana. 

A diferencia de las plataformas tradicionales de podcasts o redes sociales visuales, VocaLink está enfocada en la **comunicación conversacional fluida**. Ha sido concebida bajo el principio de **"Accesibilidad Primero" (Accessibility-First)**, garantizando que usuarios ciegos o con visión reducida disfruten de una experiencia nativa, ágil y autónoma, sin barreras de interfaz.
>>>>>>> 041cc8fa2e1e5afe35ec8d2a74e1e919dff3293a

---

## 2. Enfoque Híbrido

<<<<<<< HEAD
JEZE combina dos modalidades de comunicación para adaptarse a cada necesidad:
=======
VocaLink combina dos modalidades de comunicación para adaptarse a cada necesidad:
>>>>>>> 041cc8fa2e1e5afe35ec8d2a74e1e919dff3293a

| Dimensión | Módulo Asíncrono (Núcleo Principal) | Módulo En Vivo (Secundario / Eventos) |
| :--- | :--- | :--- |
| **Caso de Uso** | Hilos de audio, respuestas temáticas, notas de voz estructuradas. | Salas de debate espontáneo, reuniones grupales, walkie-talkie. |
| **Protocolo** | HTTP REST / gRPC + CDN Storage (S3 / Cloudflare R2). | WebRTC via SFU (LiveKit / Agora). |
| **Formato / Latencia** | Audio comprimido Opus / AAC-LC (~100-500ms). | Streaming de ultra baja latencia (&lt;200ms). |
| **Control de Usuario**| Aceleración (1.0x - 3.0x), salto de silencios, transcripción. | Petición de turno de palabra ("Levantar la mano"), moderación. |

---

## 3. Requisitos de Accesibilidad (A11y)

Cumplimiento de estándares **WCAG 2.1 Nivel AAA**:

- **Compatibilidad con Lectores de Pantalla:**
  - Etiquetado dinámico explícito (`aria-label`, `accessibilityLabel`) para **VoiceOver** (iOS), **TalkBack** (Android) y **NVDA/JAWS** (Web).
  - Anuncio contextual automático de estados (ej. *"Grabación iniciada"*, *"Mensaje enviado"*).

- **Navegación y Gestos Simplificados:**
  - Áreas de interacción táctil ampliadas (mínimo $48 \times 48 \text{ dp}$).
  - Gestos universales personalizables (ej. doble toque con dos dedos para reproducir/pausar).

- **Transcripción e Inteligencia Visual (IA):**
  - Transcripción automática Speech-to-Text (Whisper AI) procesada en segundo plano antes de la reproducción.
  - Permite al lector de pantalla inspeccionar el texto de un audio antes de escucharlo.

- **Control Acelerado sin Distorsión:**
  - Ajuste de velocidad de audio hasta **3.0x** con compensación de tono (*pitch compensation*) para usuarios acostumbrados a alto ritmo de lectura por voz.

- **Confirmaciones Auditivas y Hápticas (Audio Cues):**
  - Tonos de frecuencia diferenciados y patrones de vibración para cada acción dentro de la app.

---

## 4. Características Clave (MVP)

1. **Reproductor Continuo en Segundo Plano:** Escucha hilos conversacionales mientras navegas por la app o con la pantalla bloqueada.
2. **Hilos de Respuesta por Audio:** Estructura en árbol para responder punto por punto a mensajes específicos.
3. **Comandos de Voz Integrados:** Operatividad por instrucciones habladas (*"Responder mensaje"*, *"Siguiente hilo"*).
4. **Cancelación de Ruido Automática:** Filtros de procesamiento en cliente para asegurar la claridad de las grabaciones.
5. **Salas de Voz Interactivas:** Espacios en vivo con gestión accesible de la palabra.

---

## 5. Arquitectura Técnica

```text
[Cliente Móvil / Web]
  │── React Native / Flutter (Componentes Accesibles Nativos)
  │── WebRTC Native Client & Audio Player Engine
  │
  ├───▶ [API Gateway - FastAPI / .NET 8]
  │       │── Autenticación (JWT / OAuth2)
  │       │── Gestión de Hilos, Transcripciones y Metadatos (PostgreSQL / Redis)
  │
  ├───▶ [Audio Storage Engine - AWS S3 / Cloudflare R2]
  │       │── Almacenamiento de fragmentos de audio en formato Opus (.ogg/.m4a)
  │
  ├───▶ [Live Audio Server - LiveKit / WebRTC SFU]
  │       │── Transmisión de voz en vivo de baja latencia
  │
  └───▶ [IA Speech Worker - OpenAI Whisper / AWS Transcribe]
          │── Transcripción asíncrona, detección de idioma y resúmenes

---

## 6. 🏗️ Estructura del Proyecto

```text
JEZE/
├── backend/                    # Servidor FastAPI + Worker Whisper AI
│   ├── app/
│   │   ├── api/                # Endpoints de autenticación y audio
│   │   ├── models/             # Modelos SQLAlchemy
│   │   ├── schemas/            # Esquemas de validación Pydantic
│   │   ├── services/           # Lógica de almacenamiento y JWT
│   │   └── workers/            # Transcripción asíncrona con Whisper
│   ├── live-engine/            # Servidor para transmisión en vivo (WebRTC/LiveKit)
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/                   # Cliente Expo / React Native accesibilidad A11y
│   ├── src/
│   │   ├── accessibility/      # Adaptador de anuncios de voz
│   │   ├── components/         # Componentes con feedback táctil y auditivo
│   │   ├── hooks/
│   │   └── services/
│   ├── App.js
│   └── package.json
│
├── docs/                       # Documentación adicional de la arquitectura
├── docker-compose.yml
└── README.md                # Especificación general del proyecto

---

## 7. Hoja de Ruta (Roadmap)

    [ ] Fase 1: MVP Asíncrono y Core Accesible (Meses 1-2)

        Configuración de Backend (FastAPI / .NET) y almacenamiento S3.

        Creación de cliente con soporte comprobado en VoiceOver y TalkBack.

        Pipeline de grabación, reproducción a velocidad variable (1.0x - 3.0x) y transcripción asíncrona con Whisper.

    [ ] Fase 2: Integración En Vivo y Comandos de Voz (Meses 3-4)

        Despliegue de servidor LiveKit para salas en tiempo real.

        Implementación de control por voz nativo e hilos de respuesta en vivo.

    [ ] Fase 3: Inteligencia de Audio y Escalabilidad (Meses 5-6)

        Supresión de ruido por IA en cliente.

        Resúmenes automáticos de hilos conversacionales.

        Auditoría externa de accesibilidad WCAG 2.1 AAA.

🚀 Guía de Instalación y Ejecución
1. Backend (FastAPI & Whisper AI)

Abre una terminal (PowerShell) en la raíz de tu proyecto JEZE y ejecuta:

# Acceder a la carpeta del backend
cd backend

# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual en Windows PowerShell
.\venv\Scripts\Activate.ps1

# Instalar las dependencias
pip install -r requirements.txt

# Iniciar el servidor de desarrollo
uvicorn app.main:app --reload --port 8000

2. Frontend (Expo / React Native)

Abre otra ventana de terminal independiente en la raíz del proyecto JEZE:

# Acceder a la carpeta del frontend
cd frontend

# Instalar dependencias de JavaScript
npm install

# Iniciar la aplicación con Expo
npx expo start

📱 Probar el Sistema Completo

    1. Dispositivo Móvil: Descarga la aplicación Expo Go en tu dispositivo Android o iOS y escanea el código QR generado en la terminal de Expo.

    2. Pruebas de Accesibilidad: Activa TalkBack (Android) o VoiceOver (iOS) en la configuración de accesibilidad de tu dispositivo para validar las lecturas adaptadas y las vibraciones hápticas al grabar o reproducir notas de voz.

    3. Procesamiento de Audio: Al grabar y subir una nota de voz desde la app, la terminal del backend procesará el archivo en segundo plano usando Whisper AI para generar automáticamente la transcripción accesible.'
