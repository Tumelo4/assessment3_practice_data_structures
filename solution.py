# write your code here

from time import time


def unique_sorted(lst):
    return sorted(set(lst))

def rotate_list(lst, n):
    if not lst or n == 0:
        return lst
    n = n % len(lst)
    return lst[n:] + lst[:n]

def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

def get_intersection(lst1, lst2):
    result = []
    intersection = list(set(lst1) & set(lst2))
    for item in lst1:
        if item in intersection and not item in result:
            result.append(item)
    return result

def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

def invert_dict(d):
    return {v: k for k, v in d.items()}

def merge_sum(d1, d2):
    merged = d1.copy()
    for k, v in d2.items():
        merged[k] = merged.get(k, 0) + v
    return merged

def group_by_first_letter(words):
    groups = {}
    for word in words:
        first_letter = word[0]
        if first_letter not in groups:
            groups[first_letter] = []
        groups[first_letter].append(word)
    return groups

def multi_sort(data):
    return sorted(data, key=lambda x: (x[1], x[2], x[0]))

def calculate_tax(products, category):
    total = sum(prod["price"] for prod in products if prod["cat"] == category)
    return total + (total * 0.1)  # Assuming 10% tax rate

def is_anagram(s1, s2):
    cleaned_s1 = ''.join(c.lower() for c in s1 if c.isalnum())
    cleaned_s2 = ''.join(c.lower() for c in s2 if c.isalnum())
    return sorted(cleaned_s1) == sorted(cleaned_s2)

def unique_preserve_order(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def windowed_average(lst, window_size):
    if not lst or window_size <= 0:
        return []
    averages = []
    for i in range(len(lst) - window_size + 1):
        window = lst[i:i + window_size]
        averages.append(sum(window) / len(window))
    return averages

def deep_merge(d1, d2):
    merged = d1.copy()
    for k, v in d2.items():
        if k in merged and isinstance(merged[k], dict) and isinstance(v, dict):
            merged[k] = deep_merge(merged[k], v)
        else:
            merged[k] = v
    return merged

def normalized_char_frequency(s):
    char_list = s.strip().lower().split()
    freq = {}
    for char in char_list:
        for c in char:
            freq[c] = freq.get(c, 0) + 1
    return freq


def cartesian_product(lst1, lst2):
    return [(a, b) for a in lst1 for b in lst2]

def deep_key_search(d, key):
    if key in d:
        return d[key]
    for k, v in d.items():
        if isinstance(v, dict):
            result = deep_key_search(v, key)
            if result is not None:
                return result
    return None

def nested_flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(nested_flatten(item))
        else:
            flat_list.append(item)
    return flat_list

def stable_multi_sort(data):
    return sorted(data, key=lambda x: (-x[1], x[0]))

def validate_schema(data, schema):
    for key, expected_type in schema.items():
        if key not in data:
            return False
        if not isinstance(data[key], expected_type):
            return False
    return True
def deduplicate_records(records, key):
    seen = set()
    result = []
    for record in records:
        if key not in record:
            result.append(record)
            continue
 
        value = record[key]
        if value not in seen:
            seen.add(value)
            result.append(record)
    return result

def streaming_deduplicator(records_stream):
    unique_records = set(records_stream)
    result = []
    for record in records_stream:
        if record in unique_records:
            result.append(record)
            unique_records.remove(record)
    return result

def deep_diff(a, b, path=""):
    diffs = {}
    keys = set(a.keys()) | set(b.keys())
 
    for k in keys:
        current_path = f"{path}.{k}" if path else k
        a_val = a.get(k, None)
        b_val = b.get(k, None)
 
        if isinstance(a_val, dict) and isinstance(b_val, dict):
            diffs.update(deep_diff(a_val, b_val, current_path))
        elif a_val != b_val:
            diffs[current_path] = (a_val, b_val)
 
    return diffs

def get_by_path(d, path):
    path_char = path.split(".")
    for key in path_char:
        if isinstance(d, dict) and key in d:
            d = d[key]
        else:
            return None
    return d

def group_by_keys(records, keys):
    grouped = {}
    for record in records:
        group_key = tuple(record[k] for k in keys)
        if group_key not in grouped:
            grouped[group_key] = []
        grouped[group_key].append(record)
    return grouped

def sliding_window_max(lst, window_size):
    if not lst or window_size <= 0:
        return []
    max_values = []
    for i in range(len(lst) - window_size + 1):
        window = lst[i:i + window_size]
        max_values.append(max(window))
    return max_values

def circular_iter(lst):
    while True:
        for item in lst:
            yield item

def deep_freeze(d):
    if isinstance(d, dict):
        return frozenset((k, deep_freeze(v)) for k, v in d.items())
    elif isinstance(d, list):
        return tuple(deep_freeze(item) for item in d)
    else:
        return d
    
def reconcile_records(records1, records2):
    records = {}
    order = []

    for rec in records1:
        records[rec["id"]] = rec
        order.append(rec["id"])

    for rec in records2:
        rid = rec["id"]
        if rid in records:
            if rec["ts"] > records[rid]["ts"]:
                records[rid] = rec
        else:
            records[rid] = rec
            order.append(rid)

    return [records[rid] for rid in order]

def mask_sensitive(data, sensitive_keys):
    masked_data = {}
    for key, value in data.items():
        for sensitive_key in sensitive_keys:
            if key in sensitive_key:
                masked_data[key] = "***"
                break
            elif isinstance(value, dict):
                masked_data[key] = mask_sensitive(value, sensitive_keys)
            else:
                masked_data[key] = value
    return masked_data

def fault_tolerant_pipeline(items , funcs):
    results = []
    for item in items:
        for func in funcs:
            try:
                item = func(item)
            except Exception:
                continue
        results.append(item)
    return results

def LRUCache(capacity):
    class LRUCache:
        def __init__(self, capacity):
            from collections import OrderedDict
            self.capacity = capacity
            self.cache = OrderedDict()
    
        def get(self, key):
            if key not in self.cache:
                return None
            self.cache.move_to_end(key)
            return self.cache[key]
    
        def set(self, key, value):
            if key in self.cache:
                self.cache.move_to_end(key)
            self.cache[key] = value
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)
    return LRUCache(capacity)

def top_k_frequent(lst, k):
    from collections import Counter
    freq = Counter(lst)
    return [item for item, count in freq.most_common(k)]

def json_patch(original, patch):
    import copy
    result = copy.deepcopy(original)
 
    for operation in patch:
        op = operation["op"]
        path = operation["path"]
        keys = path.split(".")
        *parent_keys, last_key = keys
 
        target = result
        for k in parent_keys:
            if op == "add":
                target = target.setdefault(k, {})
            else:
                target = target[k]
 
        if op in ("add", "replace"):
            target[last_key] = operation["value"]
        elif op == "remove":
            del target[last_key]
        else:
            raise ValueError(f"Unsupported patch operation: {op}")
 
    return result

def deterministic_hash(obj):
    import hashlib
    import json
    obj_str = json.dumps(obj, sort_keys=True)
    return hashlib.sha256(obj_str.encode()).hexdigest()

def resolve_dependencies(tasks):
    from collections import defaultdict, deque
    graph = defaultdict(list)
    indegree = defaultdict(int)

    for task, deps in tasks.items():
        for dep in deps:
            graph[dep].append(task)
            indegree[task] += 1

    queue = deque([task for task in tasks if indegree[task] == 0])
    resolved_order = []

    while queue:
        current = queue.popleft()
        resolved_order.append(current)
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(resolved_order) != len(tasks):
        raise ValueError("Circular dependency detected")
    
    return resolved_order

def TokenBucket(capacity, refill_rate):
    class TokenBucket:
    
        def __init__(self, capacity, refill_rate):
            import time
            self.capacity = capacity
            self.refill_rate = refill_rate  # tokens added per second
            self.tokens = float(capacity)   # start full
            self.last_check = time.monotonic()
    
        def _refill(self):
            import time
            now = time.monotonic()
            elapsed = now - self.last_check
            if elapsed > 0:
                self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
                self.last_check = now
    
        def allow(self):
            self._refill()
            if self.tokens >= 1:
                self.tokens -= 1
                return True
            return False
    return TokenBucket(capacity, refill_rate)

def CircuitBreaker(failure_threshold, recovery_time):
    class CircuitBreaker:
    
        def __init__(self, failure_threshold, recovery_timeout=60):
            self.failure_threshold = failure_threshold
            self.recovery_timeout = recovery_timeout
            self.failure_count = 0
            self.state = "CLOSED"
            self.last_failure_time = None
    
        def call(self, func, *args, **kwargs):
            import time
    
            if self.state == "OPEN":
                if (
                    self.last_failure_time is not None
                    and (time.monotonic() - self.last_failure_time) >= self.recovery_timeout
                ):
                    self.state = "HALF_OPEN"
                else:
                    return None  # circuit open, reject the call without attempting it
    
            try:
                result = func(*args, **kwargs)
            except Exception:
                self.failure_count += 1
                self.last_failure_time = time.monotonic()
                if self.state == "HALF_OPEN" or self.failure_count >= self.failure_threshold:
                    self.state = "OPEN"
                return None
            else:
                # Any success resets the failure streak and closes the circuit
                self.failure_count = 0
                self.state = "CLOSED"
                return result
    return CircuitBreaker(failure_threshold, recovery_time)

def debounce_events(timestamps, wait_time):
    if not timestamps:
        return []
 
    accepted = [timestamps[0]]
    last_accepted = timestamps[0]
 
    for t in timestamps[1:]:
        if t - last_accepted >= wait_time:
            accepted.append(t)
            last_accepted = t
 
    return accepted

def migrate_schema(record, schema_map, defaults=None):
    result = {}
    for old_key, value in record.items():
        new_key = schema_map.get(old_key, old_key)
        result[new_key] = value
 
    if defaults:
        for key, default_value in defaults.items():
            result.setdefault(key, default_value)
 
    return result

def stream_join(stream1, stream2, key):
    from collections import defaultdict
    buffer = defaultdict(list)
    for record in stream2:
        buffer[record[key]].append(record)
    
    for record in stream1:
        if record[key] in buffer:
            for match in buffer[record[key]]:
                yield {**record, **match}

