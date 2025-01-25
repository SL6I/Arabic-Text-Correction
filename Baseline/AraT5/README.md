HOW TO RUN IT

python finetune_arat5.py \
  --train_file "train.json" \
  --dev_file "dev.json" \
  --test_file "test.json" \
  --output_dir "arat5_gec_checkpoints" \
  --epochs 15 \
  --learning_rate 1e-4


python predict_arat5.py \
  --model_dir "" \
  --dev_file "path/to/dev.json" \
  --test_file "path/to/test.json" \
  --output_dir "predictions" \
  --max_length 1024 \
  --num_beams 5