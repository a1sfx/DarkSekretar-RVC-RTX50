# DarkSekretar-RVC-RTX50

**Форк Mangio-RVC v23.7.0 для NVIDIA RTX 50 series (Blackwell sm_120)**

Протестировано: **RTX 5060 Ti 16GB, PyTorch 2.8.0+cu128, CUDA 12.8**

## Что исправлено

- PyTorch 2.8.0+cu128 для Blackwell (sm_120)
- Отключён DDP/Distributed для одного GPU
- Исправлен fairseq torch.load (weights_only=False)
- Исправлены тензоры в vc_infer_pipeline
- Добавлен logger, убран TensorBoard writer

## Установка

git clone https://github.com/a1sfx/DarkSekretar-RVC-RTX50.git
cd DarkSekretar-RVC-RTX50
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
pip install -r requirements.txt
python infer-web.py

## Автор

DarkSekretar (a1sfx)
